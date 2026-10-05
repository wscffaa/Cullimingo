part of 'cull_page.dart';

/// True when running under `flutter_test`, which exports `FLUTTER_TEST=true`.
/// Used to keep the card auto-mount from spawning real subprocesses in tests.
final bool _underTest = Platform.environment.containsKey('FLUTTER_TEST');

/// Folder/card ingest, workspace tabs, refresh and sidecar sync.
mixin _CullWorkspace on _CullGrid {
  // Polls for newly-mounted cards + notices when the open folder vanishes.
  Timer? _cardPollTimer;

  Set<String> _seenVolumes = const {};

  // Removable devices we've already offered to mount, so a card the user
  // manually unmounted isn't fought over (see [autoMountNewRemovables]).
  Set<String> _knownRemovables = const {};

  bool _cardsPrimed = false;

  // The folder currently shown in the grid, to detect ejection/deletion.
  String? _openSourcePath;

  // True while reopening last session's folders, to suppress re-persisting the
  // open-folders list on each intermediate tab change.
  bool _restoringFolders = false;

  // Whether "Open folder" scans sub-folders (toggle in the toolbar).
  bool _includeSubfolders = true;

  // True while a poll's listVolumes() call is still in flight, so a stuck
  // card/reader (blocking well past _volumePollStallTimeout) can't pile up
  // one spawned isolate per 3-second tick.
  bool _pollBusy = false;

  // How long a single poll waits for listVolumes() before giving up on this
  // tick and trying again next time — generous, since a healthy poll returns
  // near-instantly and this only ever fires on a genuinely failing device.
  static const _volumePollStallTimeout = Duration(seconds: 10);

  /// Periodic check: surface newly-inserted cards, and notice when the folder
  /// on screen has been ejected or deleted.
  Future<void> _pollFilesystem() async {
    if (_pollBusy) return;
    _pollBusy = true;
    try {
      // Active folder gone? (card ejected, folder deleted) → close its tab and
      // fall back to a neighbour, then tell the user.
      final src = _openSourcePath;
      // Async on purpose: this stat is the one that detects a yanked SD card
      // or hung network share — exactly the volumes where a *sync* stat can
      // block the UI isolate for minutes (the rest of this poll already hops
      // to an isolate for the same reason).
      // ignore: avoid_slow_async_io
      if (src != null && !await Directory(src).exists()) {
        final tabs = ref.read(workspaceProvider).tabs;
        final idx = tabs.indexWhere((t) => t.sourcePath == src);
        if (idx >= 0) ref.read(workspaceProvider.notifier).close(idx);
        _restoreActiveLiveState();
        if (mounted) {
          _notify(
            '文件夹已不可用（已弹出或删除）',
            kind: NoticeKind.warning,
          );
        }
      }

      // macOS auto-mounts inserted cards; many Linux desktops don't. Mount any
      // freshly-plugged removable card ourselves first, so listVolumes() below
      // sees it the same as it would on macOS. Skipped under `flutter_test` so
      // widget tests never shell out to lsblk/udisksctl (a real subprocess
      // would outlive the fake-async widget tree and leave a pending timer).
      if (Platform.isLinux && !_underTest) {
        _knownRemovables = await autoMountNewRemovables(_knownRemovables);
        if (!mounted) return;
      }

      List<Volume> volumes;
      try {
        volumes = await _listVolumesOffUiIsolate().timeout(
          _volumePollStallTimeout,
        );
      } on TimeoutException {
        // A mounted volume is failing to respond; skip this tick and keep the
        // previous baseline so a plugged-in card isn't wrongly reported as
        // removed. listVolumes() runs on its own isolate, so this only drops
        // one poll — it never blocks the UI.
        appTalker.warning(
          'listVolumes() timed out — a mounted volume may be unresponsive',
        );
        return;
      }
      if (!mounted) return;
      // First poll just primes the baseline; later ones offer newly-seen cards.
      if (_cardsPrimed) {
        newCards(_seenVolumes, volumes).forEach(_offerCardImport);
      }
      _seenVolumes = volumes.map((v) => v.path).toSet();
      _cardsPrimed = true;
    } finally {
      _pollBusy = false;
    }
  }

  /// Runs [listVolumes] on a one-off background isolate: it's fully
  /// synchronous internally, so a failing card reader can block it for a long
  /// time, and only a real isolate hop (not a same-isolate `.timeout()`) can
  /// keep that from freezing the UI. Skipped under `flutter_test`, same as
  /// [autoMountNewRemovables] above — a real isolate round-trip doesn't
  /// resolve deterministically inside the fake-async widget-test clock and
  /// would leave a "pending timer" behind.
  Future<List<Volume>> _listVolumesOffUiIsolate() =>
      _underTest ? listVolumes() : Isolate.run(listVolumes);

  void _offerCardImport(Volume card) {
    // With the auto-open preference on (Settings → General → Ingest), an
    // inserted card opens the Import dialog directly, preselected on the card
    // — unless one is already up (second card / user got there first), where
    // stacking a second modal would only get in the way.
    if (ref.read(autoOpenImportOnCardInsertProvider) && !_ingestDialogOpen) {
      unawaited(_ingest(card.path));
      return;
    }
    _showNotice(
      Notice(
        kind: NoticeKind.info,
        icon: Icons.sd_card,
        message: "检测到存储卡“${card.name}”",
        actions: [
          (
            label: '导入',
            onTap: () {
              _dismissNotice();
              unawaited(_ingest(card.path));
            },
          ),
          (
            label: 'Open',
            onTap: () {
              _dismissNotice();
              unawaited(_importFolder(card.path));
            },
          ),
        ],
      ),
    );
  }

  Future<void> _openFolder() async {
    final dir = await getDirectoryPath();
    if (dir != null) await _importFolder(dir, recursive: _includeSubfolders);
  }

  /// Toggles whether sub-folders are included and immediately re-scans the open
  /// folder so the grid reflects the change live (turning it off drops the
  /// sub-folder photos, turning it on brings them back). No-op with no folder.
  void _setIncludeSubfolders(bool value) {
    if (value == _includeSubfolders) return;
    setState(() => _includeSubfolders = value);
    unawaited(_refreshFolder());
  }

  /// Opens folder(s) dropped onto the window (`BUILD_PLAN.md` §5 Phase 1). A
  /// dropped folder opens directly; a dropped file opens its containing folder.
  Future<void> _handleDrop(DropDoneDetails details) async {
    final roots = droppedFoldersToOpen(
      details.files.map((f) => f.path),
      isDirectory: FileSystemEntity.isDirectorySync,
    );
    for (final root in roots) {
      await _importFolder(root, recursive: _includeSubfolders);
    }
  }

  void _closeActiveTab() {
    final ws = ref.read(workspaceProvider);
    if (ws.tabs.isNotEmpty) _closeTab(ws.activeIndex);
  }

  // True while the ingest dialog is up, so a card inserted meanwhile doesn't
  // auto-open a second one on top.
  bool _ingestDialogOpen = false;

  /// Opens the Phase 3 ingest dialog (optionally preselecting [source], e.g. a
  /// just-inserted card); if it returns a destination root (the import ran),
  /// opens that folder in the grid.
  Future<void> _ingest([String? source]) async {
    _ingestDialogOpen = true;
    final String? dest;
    try {
      dest = await showDialog<String>(
        context: context,
        builder: (_) => IngestDialog(initialSource: source),
      );
    } finally {
      _ingestDialogOpen = false;
    }
    if (dest == null) return;
    await _importFolder(dest);
    // Ingest is the one moment we stamp the whole import (open-folder mustn't).
    final importId = ref.read(currentImportProvider);
    if (importId == null) return;
    final stamped = await applyIngestTemplateToImport(ref, importId);
    if (stamped > 0 && mounted) {
      _notify(
        '已将元数据模板盖印到 $stamped 张导入照片',
        kind: NoticeKind.success,
      );
    }
  }

  /// Re-reads XMP sidecars from disk for the open folder and reconciles them
  /// with the read model (picks up ratings/labels/keywords edited in C1/LR).
  /// Surfaces how many photos changed and how many clashed (§4).
  Future<void> _resyncSidecars() async {
    final importId = ref.read(currentImportProvider);
    if (importId == null) return;
    final result = await ref
        .read(metadataRepositoryProvider)
        .syncSidecarsFromDisk(importId);
    if (!mounted) return;
    final conflicts = result.conflicts > 0
        ? ' · ${result.conflicts} 个冲突'
        : '';
    final message = result.isEmpty
        ? '附属文件已是最新'
        : '已从磁盘更新 ${result.updated} 张照片$conflicts';
    _notify(
      message,
      kind: result.conflicts > 0 ? NoticeKind.warning : NoticeKind.success,
    );
  }

  Future<void> _applyTemplate() async {
    final outcome = await applySavedTemplateToSelection(ref);
    if (!mounted) return;
    switch (outcome.result) {
      case ApplyTemplateResult.noTemplate:
        _notify(
          '尚未设置元数据模板——请在设置中添加',
          kind: NoticeKind.warning,
        );
      case ApplyTemplateResult.noTargets:
        _notify('请选择要应用模板的照片');
      case ApplyTemplateResult.applied:
        _notify(
          '已将元数据模板应用到 ${outcome.count} 张照片',
          kind: NoticeKind.success,
        );
    }
    _gridFocus.requestFocus();
  }

  /// Batch "From GPS": stamps the geocoded location onto the selection and
  /// reports what happened (photos without a position are just skipped).
  Future<void> _geocodeSelection() async {
    final outcome = await geocodeSelection(ref);
    if (!mounted) return;
    final skipped = [
      if (outcome.noGps > 0) '${outcome.noGps} 张无 GPS',
      if (outcome.noPlace > 0) '${outcome.noPlace} 张附近无地点',
    ].join(' · ');
    if (outcome.filled == 0) {
      _notify(
        skipped.isEmpty
            ? '请选择照片以从 GPS 填充位置'
            : '未填充位置——$skipped',
        kind: NoticeKind.warning,
      );
    } else {
      _notify(
        "已为 ${outcome.filled} 张照片填充位置${skipped.isEmpty ? '' : ' · $skipped'}",
        kind: NoticeKind.success,
      );
    }
    _gridFocus.requestFocus();
  }

  Future<void> _clearCache() async {
    await ref.read(previewCacheProvider).clear();
    // Drop decoded images too, so freed disk/RAM is actually reclaimed.
    PaintingBinding.instance.imageCache.clear();
    if (!mounted) return;
    _notify('缩略图缓存已清除', kind: NoticeKind.success);
  }

  // Saves the live focus/selection + filter + scroll into the active tab
  // (before a switch) so re-selecting that tab restores where you were.
  void _saveActiveLiveState() {
    ref
        .read(workspaceProvider.notifier)
        .saveActive(
          selection: ref.read(cullControllerProvider),
          filter: ref.read(photoFilterControllerProvider),
          sort: ref.read(photoSortControllerProvider),
          scrollOffset: _scroll.hasClients ? _scroll.offset : 0,
        );
  }

  // Loads the active tab's saved view into the live controllers (after a switch
  // or close); falls back to defaults when no tab is open. The scroll offset is
  // applied once the new grid has laid out (see [_pendingScrollRestore]) — a
  // fresh tab restores to 0, so its top previews load instead of landing mid
  // list at the previous tab's offset (cells above wouldn't have decoded).
  void _restoreActiveLiveState() {
    final tab = ref.read(workspaceProvider).active;
    ref
        .read(cullControllerProvider.notifier)
        .restore(tab?.selection ?? const CullSelection());
    ref
        .read(photoFilterControllerProvider.notifier)
        .restore(tab?.filter ?? const PhotoFilter());
    ref
        .read(photoSortControllerProvider.notifier)
        .restore(tab?.sort ?? const PhotoSort());
    _openSourcePath = tab?.sourcePath;
    _pendingScrollRestore = tab?.scrollOffset ?? 0;
  }

  void _switchTab(int index) {
    if (index == ref.read(workspaceProvider).activeIndex) return;
    _saveActiveLiveState();
    ref.read(workspaceProvider.notifier).activate(index);
    _restoreActiveLiveState();
    _gridFocus.requestFocus();
  }

  void _closeTab(int index) {
    final wasActive = index == ref.read(workspaceProvider).activeIndex;
    ref.read(workspaceProvider.notifier).close(index);
    // Only reload when the active tab actually changed — closing a background
    // tab must not clobber the live tab's unsaved selection.
    if (wasActive) _restoreActiveLiveState();
  }

  Future<void> _importFolder(String dir, {bool recursive = true}) async {
    final repo = ref.read(libraryRepositoryProvider);
    // Remember it for the "Open recent" menu (dedup + capped in the provider).
    ref.read(recentFoldersProvider.notifier).add(dir);
    // Reuse the import if this folder was opened before (so it opens again),
    // else create + populate. Select first so the grid is live immediately.
    final (importId, isNew) = await repo.findOrCreateImport(dir);
    // Open as a tab: save the current tab's view, switch, restore the new one's
    // (a fresh tab restores to defaults; a re-opened one to where you left it).
    _saveActiveLiveState();
    ref
        .read(workspaceProvider.notifier)
        .openImport(
          importId: importId,
          sourcePath: dir,
          label: p.basename(dir),
        );
    _restoreActiveLiveState();
    _gridFocus.requestFocus();
    if (isNew) {
      await repo.populateImport(importId, dir, recursive: recursive);
    } else {
      // Re-opening a known folder re-scans it (§4): pick up files added/removed
      // on disk *and* ratings/labels/keywords edited in C1/LR since last time.
      // Background so the grid shows instantly; a notice only if something
      // changed. Rescanning here also heals an import left empty (e.g. first
      // opened with subfolders off), so opening a folder always shows its
      // current contents.
      unawaited(_backgroundResync(importId, dir));
    }
  }

  /// Reopens the folders open in the last session (newest tab last), if the
  /// user enabled it. Folders that no longer exist (ejected card, deleted dir)
  /// are skipped with a notice. Runs once at startup.
  Future<void> _restoreLastFolders() async {
    final settings = await AppSettings.load();
    if (!settings.reopenLastFolders || !mounted) return;
    final folders = settings.lastFolders;
    if (folders.isEmpty) return;
    final activeIndex = settings.lastActiveTab;
    _restoringFolders = true;
    var missing = 0;
    try {
      for (final dir in folders) {
        if (!mounted) break;
        if (Directory(dir).existsSync()) {
          await _importFolder(dir);
        } else {
          missing++;
        }
      }
    } finally {
      _restoringFolders = false;
    }
    if (!mounted) return;
    // Re-activate the tab that was active last session (clamped in case some
    // folders went missing), so you land where you left off.
    final tabs = ref.read(workspaceProvider).tabs;
    if (tabs.isNotEmpty) {
      ref
          .read(workspaceProvider.notifier)
          .activate(activeIndex.clamp(0, tabs.length - 1));
      _restoreActiveLiveState();
    }
    if (missing > 0) {
      _notify(
        '$missing 个已保存的文件夹不再可用',
        kind: NoticeKind.warning,
      );
    }
    // Re-persist so vanished folders drop out of the saved list.
    _persistOpenFolders();
  }

  /// Remembers the open folders' paths (tab order) + the active tab so the next
  /// launch can reopen them. No-op while restoring (avoids churn mid-restore).
  void _persistOpenFolders() {
    if (_restoringFolders) return;
    final ws = ref.read(workspaceProvider);
    final paths = [for (final t in ws.tabs) t.sourcePath];
    unawaited(
      updateSettings(
        (s) => s.setLastFoldersWithActive(paths, ws.activeIndex),
      ),
    );
  }

  /// Re-scans the active folder for files added or deleted on disk
  /// (⌘/Ctrl+R). New files appear with their marks read; local edits on
  /// existing photos are preserved. No-op when no folder is open.
  Future<void> _refreshFolder() async {
    final importId = ref.read(currentImportProvider);
    final root = _openSourcePath;
    if (importId == null || root == null) return;
    final result = await ref
        .read(libraryRepositoryProvider)
        .refreshImport(importId, root, recursive: _includeSubfolders);
    _evictChangedPreviews(result.changedPaths);
    if (!mounted) return;
    if (result.unavailable) {
      _notify(
        '无法刷新：文件夹缺失或为空——存储卡或驱动器是否已连接？未删除任何内容。',
        kind: NoticeKind.warning,
      );
      return;
    }
    if (result.unreadable > 0) {
      _notify(
        '已刷新：+${result.added} 张照片，但 ${result.unreadable} 个项目无法读取——未删除任何内容。请检查存储卡或驱动器及其权限。',
        kind: NoticeKind.warning,
      );
      return;
    }
    final upToDate =
        result.added == 0 && result.removed == 0 && result.changedPaths.isEmpty;
    _notify(
      upToDate
          ? '文件夹已是最新'
          : "已刷新：+${result.added} / −${result.removed} 张${result.changedPaths.isEmpty ? '' : ' · ${result.changedPaths.length} 张有改动'}",
      kind: upToDate ? NoticeKind.info : NoticeKind.success,
    );
  }

  /// Drops the RAM previews of externally changed files so the grid/loupe
  /// re-decode — the RAM tier is keyed by path alone (the disk tier
  /// self-invalidates via the mtime in its key).
  void _evictChangedPreviews(List<String> paths) {
    if (paths.isEmpty) return;
    paths.forEach(ref.read(previewCacheProvider).evict);
  }

  Future<void> _backgroundResync(int importId, String root) async {
    // First re-scan for files added/removed on disk (recursively per the
    // toggle), so a reopened folder reflects its current contents — and an
    // empty import finally populates. Then sync marks edited externally.
    final scan = await ref
        .read(libraryRepositoryProvider)
        .refreshImport(importId, root, recursive: _includeSubfolders);
    // Folder gone or listing empty (drive unplugged): keep everything as is.
    if (scan.unavailable) return;
    if (mounted) _evictChangedPreviews(scan.changedPaths);
    final marks = await ref
        .read(metadataRepositoryProvider)
        .syncSidecarsFromDisk(importId);
    if (!mounted) return;

    final scanChanged =
        scan.added > 0 || scan.removed > 0 || scan.changedPaths.isNotEmpty;
    // A partial listing is worth a word even when nothing else changed: the
    // folder holds files this session can't see.
    if (!scanChanged && marks.isEmpty && scan.unreadable == 0) return;

    final parts = <String>[
      if (scanChanged) '+${scan.added} / −${scan.removed} 个文件',
      if (marks.updated > 0) '来自磁盘的 ${marks.updated} 条标记',
    ];
    final conflicts = marks.conflicts > 0
        ? ' · ${marks.conflicts} 个冲突'
        : '';
    final unreadable = scan.unreadable > 0
        ? "${parts.isEmpty ? '' : ' · '}${scan.unreadable} 个项目无法读取"
        : '';
    _notify(
      '已同步 ${parts.join(' · ')}$conflicts$unreadable',
      kind: marks.conflicts > 0 || scan.unreadable > 0
          ? NoticeKind.warning
          : NoticeKind.success,
    );
  }
}
