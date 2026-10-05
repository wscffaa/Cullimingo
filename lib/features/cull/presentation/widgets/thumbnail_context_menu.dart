import 'package:cullimingo/app/theme/tokens.dart';
import 'package:cullimingo/core/db/database.dart';
import 'package:cullimingo/core/files/open_external.dart';
import 'package:cullimingo/features/cull/presentation/cull_providers.dart';
import 'package:cullimingo/features/handoff/data/transfer_service.dart';
import 'package:cullimingo/features/handoff/domain/external_editor.dart';
import 'package:cullimingo/features/handoff/presentation/send_to_providers.dart';
import 'package:cullimingo/features/metadata/presentation/keyword_dialog.dart';
import 'package:cullimingo/shared/models/cull_marks.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

/// A context-menu entry's deferred action, run after the menu closes.
typedef _MenuAction = Future<void> Function();

/// Right-click menu for a grid thumbnail. Acts on the current selection when
/// [photo] is part of it, otherwise on [photo] alone — the caller arranges the
/// selection (via selectOnly / focus) before opening so the controller's
/// batch helpers ([CullController.applyRating] etc.) target the right photos.
///
/// Each entry's value is the action to run; rating / flag / colour are compact
/// palette rows so a mark is one click away (Photo Mechanic style).
Future<void> showThumbnailContextMenu({
  required BuildContext context,
  required WidgetRef ref,
  required Photo photo,
  required Offset globalPosition,
  required ValueChanged<TransferMode> onTransfer,
  required ValueChanged<ExternalEditor> onSendTo,
  VoidCallback? onEditMetadata,
  VoidCallback? onRename,
  VoidCallback? onApplyTemplate,
  VoidCallback? onGeocode,
  VoidCallback? onExport,
  VoidCallback? onExpandBrackets,
  VoidCallback? onApplyMarksToBracket,
  VoidCallback? onStack,
  VoidCallback? onUnstack,
  ValueChanged<bool>? onContactSheet,
  VoidCallback? onDelete,
}) async {
  final overlay = Overlay.of(context).context.findRenderObject()! as RenderBox;
  final position = RelativeRect.fromRect(
    Rect.fromPoints(globalPosition, globalPosition),
    Offset.zero & overlay.size,
  );
  final controller = ref.read(cullControllerProvider.notifier);
  final count = ref.read(cullControllerProvider).markTargets.length;
  // Configured "Send to" editors (empty when none set / not yet loaded); the
  // menu adds an "Open in <editor>" row per entry. Read synchronously — the
  // page keeps this provider warm — so opening the menu stays instant.
  final editors =
      ref.read(sendToEditorsProvider).value ?? const <ExternalEditor>[];

  final action = await showMenu<_MenuAction>(
    context: context,
    position: position,
    color: AppColors.surfaceElevated,
    popUpAnimationStyle: kMenuAnimationStyle,
    menuPadding: const EdgeInsets.symmetric(vertical: AppSpacing.xs),
    items: [
      if (count > 1)
        PopupMenuItem<_MenuAction>(
          enabled: false,
          height: 32,
          child: Text(
            '$count 张照片',
            style: const TextStyle(
              color: AppColors.textSecondary,
              fontSize: 12,
              fontWeight: FontWeight.w600,
            ),
          ),
        ),
      PopupMenuItem<_MenuAction>(
        enabled: false,
        padding: EdgeInsets.zero,
        child: _RatingRow(photo: photo, controller: controller),
      ),
      PopupMenuItem<_MenuAction>(
        enabled: false,
        padding: EdgeInsets.zero,
        child: _FlagRow(photo: photo, controller: controller),
      ),
      PopupMenuItem<_MenuAction>(
        enabled: false,
        padding: EdgeInsets.zero,
        child: _ColorRow(photo: photo, controller: controller),
      ),
      const PopupMenuDivider(height: 8),
      _action(
        () => controller.applyRotation(-1),
        const _MenuRow('向左旋转', ','),
      ),
      _action(
        () => controller.applyRotation(1),
        const _MenuRow('向右旋转', '.'),
      ),
      const PopupMenuDivider(height: 8),
      if (onEditMetadata != null)
        _action(
          () async => onEditMetadata(),
          const _MenuRow('编辑元数据…', 'M'),
        ),
      _action(
        () => showKeywordEditor(context, ref),
        const _MenuRow('编辑关键字…', 'K'),
      ),
      if (onApplyTemplate != null)
        _action(
          () async => onApplyTemplate(),
          const _MenuRow('应用元数据模板', 'T'),
        ),
      if (onGeocode != null)
        _action(() async => onGeocode(), const Text('从 GPS 填充位置')),
      const PopupMenuDivider(height: 8),
      if (onExpandBrackets != null)
        _action(
          () async => onExpandBrackets(),
          const _MenuRow('扩展选择到包围曝光', 'G'),
        ),
      if (onApplyMarksToBracket != null)
        _action(
          () async => onApplyMarksToBracket(),
          const Text('应用标记到包围曝光'),
        ),
      if (onStack != null)
        _action(() async => onStack(), const Text('堆叠为包围曝光')),
      if (onUnstack != null)
        _action(() async => onUnstack(), const Text('从包围曝光中移除')),
      if (onRename != null)
        _action(() async => onRename(), const _MenuRow('重命名…', 'R')),
      _action(
        () async => onTransfer(TransferMode.copy),
        const Text('复制到文件夹…'),
      ),
      _action(
        () async => onTransfer(TransferMode.move),
        const Text('移动到文件夹…'),
      ),
      if (onExport != null)
        _action(() async => onExport(), const _MenuRow('导出…', 'S')),
      // ContactSheet round-trip — only when the integration is configured
      // (the caller passes a non-null callback in that case, §7b).
      if (onContactSheet != null) ...[
        const PopupMenuDivider(height: 8),
        _action(
          () async => onContactSheet(false),
          const Text('发送到 ContactSheet…'),
        ),
        _action(
          () async => onContactSheet(true),
          const Text('从 ContactSheet 拉取标记…'),
        ),
      ],
      const PopupMenuDivider(height: 8),
      _action(
        () => openExternally(photo.path),
        const Text('在默认应用中打开'),
      ),
      _action(
        () => revealInFileManager(photo.path),
        Text(revealInFileManagerLabel),
      ),
      if (editors.isNotEmpty) ...[
        const PopupMenuDivider(height: 8),
        for (final editor in editors)
          _action(
            () async => onSendTo(editor),
            Text('在 ${editor.label} 中打开'),
          ),
      ],
      // Destructive, so it sits alone behind a divider (mirrors the toolbar's
      // "Delete rejected photos" placement in cull_top_bar.dart).
      if (onDelete != null) ...[
        const PopupMenuDivider(height: 8),
        _action(
          () async => onDelete(),
          const Text(
            '删除…',
            style: TextStyle(color: AppColors.labelRed),
          ),
        ),
      ],
    ],
  );
  await action?.call();
}

/// A compact action row — shorter than the 48px `PopupMenuItem` default so the
/// (long) thumbnail menu stays within the window height (spacing-only trim).
PopupMenuItem<_MenuAction> _action(_MenuAction value, Widget child) =>
    PopupMenuItem<_MenuAction>(height: 36, value: value, child: child);

/// A menu label with a right-aligned, muted shortcut hint (Photo-Mechanic
/// style, e.g. `Apply metadata template … T`).
class _MenuRow extends StatelessWidget {
  const _MenuRow(this.label, this.shortcut);

  final String label;
  final String shortcut;

  @override
  Widget build(BuildContext context) => Row(
    children: [
      Expanded(child: Text(label)),
      const SizedBox(width: AppSpacing.lg),
      Text(
        shortcut,
        style: const TextStyle(
          color: AppColors.textSecondary,
          fontSize: 12,
        ),
      ),
    ],
  );
}

/// Five stars that set the rating (clicking the current one clears it).
class _RatingRow extends StatelessWidget {
  const _RatingRow({required this.photo, required this.controller});

  final Photo photo;
  final CullController controller;

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        for (var i = 1; i <= 5; i++)
          IconButton(
            iconSize: 18,
            visualDensity: VisualDensity.compact,
            tooltip: '评 $i 星',
            icon: Icon(
              i <= photo.rating
                  ? Icons.star_rounded
                  : Icons.star_outline_rounded,
              color: i <= photo.rating
                  ? AppColors.ratingGold
                  : AppColors.textSecondary,
            ),
            onPressed: () => Navigator.pop(
              context,
              () => controller.applyRating(photo.rating == i ? 0 : i),
            ),
          ),
      ],
    );
  }
}

/// Pick / Reject / clear flag.
class _FlagRow extends StatelessWidget {
  const _FlagRow({required this.photo, required this.controller});

  final Photo photo;
  final CullController controller;

  @override
  Widget build(BuildContext context) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        IconButton(
          iconSize: 18,
          visualDensity: VisualDensity.compact,
          tooltip: 'Pick',
          icon: Icon(
            Icons.check_rounded,
            color: photo.flag == PickFlag.pick
                ? AppColors.selection
                : AppColors.textSecondary,
          ),
          onPressed: () => Navigator.pop(
            context,
            () => controller.applyFlag(
              photo.flag == PickFlag.pick ? PickFlag.none : PickFlag.pick,
            ),
          ),
        ),
        IconButton(
          iconSize: 18,
          visualDensity: VisualDensity.compact,
          tooltip: '剔除',
          icon: Icon(
            Icons.close_rounded,
            color: photo.flag == PickFlag.reject
                ? AppColors.labelRed
                : AppColors.textSecondary,
          ),
          onPressed: () => Navigator.pop(
            context,
            () => controller.applyFlag(
              photo.flag == PickFlag.reject ? PickFlag.none : PickFlag.reject,
            ),
          ),
        ),
      ],
    );
  }
}

/// Colour-label swatches plus a "none" chip.
class _ColorRow extends StatelessWidget {
  const _ColorRow({required this.photo, required this.controller});

  final Photo photo;
  final CullController controller;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.symmetric(
        horizontal: AppSpacing.md,
        vertical: AppSpacing.xs,
      ),
      child: Row(
        mainAxisSize: MainAxisSize.min,
        children: [
          for (final label in ColorLabel.values)
            if (label != ColorLabel.none)
              Padding(
                padding: const EdgeInsets.only(right: AppSpacing.sm),
                child: GestureDetector(
                  onTap: () => Navigator.pop(
                    context,
                    () => controller.applyColor(
                      photo.colorLabel == label ? ColorLabel.none : label,
                    ),
                  ),
                  child: Container(
                    width: 18,
                    height: 18,
                    decoration: BoxDecoration(
                      color: label.color,
                      shape: BoxShape.circle,
                      border: Border.all(
                        color: photo.colorLabel == label
                            ? Colors.white
                            : Colors.black.withValues(alpha: 0.4),
                        width: photo.colorLabel == label ? 2 : 1,
                      ),
                    ),
                  ),
                ),
              ),
        ],
      ),
    );
  }
}
