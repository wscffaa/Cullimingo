# Cullimingo 简体中文翻译对照表（zh-cn 本地化分支）

- 基线：上游 v1.4.0 tag（分支 `zh-cn`），仅翻译 `lib/features/` 与 `lib/shared/` 下的用户可见 UI 字符串。
- 目的：上游升级后重打补丁时逐条核对。英文列与源码中的字符串字面量一致（含 `$var` / `${expr}` 插值占位符，重打补丁时必须原样保留）。
- 未翻译（刻意保留英文）：XMP/IPTC 内部键名（如 `LocationShown`、`photoshop:Source`）、FTP 协议命令、文件扩展名、品牌与产品名（Cullimingo、Lightroom、Capture One、ContactSheet、Photo Mechanic、Adobe Bridge）、键盘按键名（⌘/Ctrl 组合）、示例数据（`_AIV9551 …`、`DSC0001.ARW`、`ILCE-7M4`）、日志输出（`debugPrint`/`appTalker` 等）。
- 复数处理：英文 `photo${n == 1 ? '' : 's'}` 类插值在中文里无单复数，统一简化为「N 张照片」，占位变量保持不变。

共 785 条对照。

| 英文 | 中文 | 所在文件 |
| --- | --- | --- |
| `Apply metadata template` | 应用元数据模板 | `features/cull/domain/cull_shortcuts.dart` |
| `Backspace` | 退格 | `features/cull/domain/cull_shortcuts.dart` |
| `Clear rating` | 清除星级 | `features/cull/domain/cull_shortcuts.dart` |
| `Colour: blue` | 色标：蓝 | `features/cull/domain/cull_shortcuts.dart` |
| `Colour: green` | 色标：绿 | `features/cull/domain/cull_shortcuts.dart` |
| `Colour: purple` | 色标：紫 | `features/cull/domain/cull_shortcuts.dart` |
| `Colour: red` | 色标：红 | `features/cull/domain/cull_shortcuts.dart` |
| `Colour: yellow` | 色标：黄 | `features/cull/domain/cull_shortcuts.dart` |
| `Compare focused photo's group` | 对比焦点照片的组 | `features/cull/domain/cull_shortcuts.dart` |
| `Compare selected` | 对比已选 | `features/cull/domain/cull_shortcuts.dart` |
| `Edit keywords` | 编辑关键字 | `features/cull/domain/cull_shortcuts.dart` |
| `Edit metadata` | 编辑元数据 | `features/cull/domain/cull_shortcuts.dart` |
| `Enter` | 回车 | `features/cull/domain/cull_shortcuts.dart` |
| `Expand selection to bracket` | 扩展选择到包围曝光 | `features/cull/domain/cull_shortcuts.dart` |
| `Info inspector` | 信息检查器 | `features/cull/domain/cull_shortcuts.dart` |
| `Loupe` | 放大视图 | `features/cull/domain/cull_shortcuts.dart` |
| `Pick` | 精选 | `features/cull/domain/cull_shortcuts.dart` |
| `Rate 1` | 评 1 星 | `features/cull/domain/cull_shortcuts.dart` |
| `Rate 2` | 评 2 星 | `features/cull/domain/cull_shortcuts.dart` |
| `Rate 3` | 评 3 星 | `features/cull/domain/cull_shortcuts.dart` |
| `Rate 4` | 评 4 星 | `features/cull/domain/cull_shortcuts.dart` |
| `Rate 5` | 评 5 星 | `features/cull/domain/cull_shortcuts.dart` |
| `Rename…` | 重命名… | `features/cull/domain/cull_shortcuts.dart` |
| `Rotate left` | 向左旋转 | `features/cull/domain/cull_shortcuts.dart` |
| `Rotate right` | 向右旋转 | `features/cull/domain/cull_shortcuts.dart` |
| `Select` | 选择 | `features/cull/domain/cull_shortcuts.dart` |
| `Space` | 空格 | `features/cull/domain/cull_shortcuts.dart` |
| `Tab` | Tab | `features/cull/domain/cull_shortcuts.dart` |
| `Delete` | 删除 | `features/cull/domain/cull_shortcuts.dart、features/cull/presentation/widgets/cull_top_bar.dart、features/filter/presentation/filter_bar.dart` |
| `Reject` | 剔除 | `features/cull/domain/cull_shortcuts.dart、features/cull/presentation/widgets/thumbnail_context_menu.dart、features/inspector/presentation/inspector_panel.dart` |
| `$noun ($photoCount photos)` | $noun（$photoCount 张） | `features/cull/domain/mark_undo.dart` |
| `colour label` | 色标 | `features/cull/domain/mark_undo.dart` |
| `flag` | 标记 | `features/cull/domain/mark_undo.dart` |
| `rating` | 星级 | `features/cull/domain/mark_undo.dart` |
| `rotation` | 旋转 | `features/cull/domain/mark_undo.dart` |
| `stack` | 堆叠 | `features/cull/domain/mark_undo.dart` |
| `unstack` | 取消堆叠 | `features/cull/domain/mark_undo.dart` |
| `Balanced` | 均衡 | `features/cull/domain/similarity_sensitivity.dart` |
| `Loose` | 宽松 | `features/cull/domain/similarity_sensitivity.dart` |
| `Near-duplicates only` | 仅近似重复 | `features/cull/domain/similarity_sensitivity.dart` |
| `Same subject / burst` | 同主体 / 连拍 | `features/cull/domain/similarity_sensitivity.dart` |
| `Similar scenes` | 相似场景 | `features/cull/domain/similarity_sensitivity.dart` |
| `Strict` | 严格 | `features/cull/domain/similarity_sensitivity.dart` |
| `Exporting` | 导出 | `features/cull/presentation/background_jobs.dart` |
| `Finding similar` | 查找相似 | `features/cull/presentation/background_jobs.dart` |
| `Export` | 导出 | `features/cull/presentation/background_jobs.dart、features/cull/presentation/widgets/export_bar.dart、features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart、features/export/presentation/export_dialog.dart` |
| `$renderFailed failed to render` | $renderFailed 张渲染失败 | `features/cull/presentation/cull_job_runner.dart` |
| `$savedCollections collection(s)` | $savedCollections 个收藏 | `features/cull/presentation/cull_job_runner.dart` |
| `${failures.length} failed to upload (${failures.first.error})` | ${failures.length} 个上传失败（${failures.first.error}） | `features/cull/presentation/cull_job_runner.dart` |
| `${isMove ? 'Move' : 'Copy'} not started: ${check.problems.join(' ')}` | 无法开始${isMove ? '移动' : '复制'}：${check.problems.join(' ')} | `features/cull/presentation/cull_job_runner.dart` |
| `${isMove ? 'Moved' : 'Copied'} ${summary.transferred} photo(s)` | 已${isMove ? '移动' : '复制'} ${summary.transferred} 张照片 | `features/cull/presentation/cull_job_runner.dart` |
| `${resolved.length} marked photo(s)` | ${resolved.length} 张已标记照片 | `features/cull/presentation/cull_job_runner.dart` |
| `${summary.conflicts} skipped (name in use)` | ${summary.conflicts} 个跳过（名称被占用） | `features/cull/presentation/cull_job_runner.dart` |
| `${summary.failed} failed` | ${summary.failed} 个失败 | `features/cull/presentation/cull_job_runner.dart` |
| `${summary.stillBeingWritten} still being written (retry)` | ${summary.stillBeingWritten} 个仍在写入（请重试） | `features/cull/presentation/cull_job_runner.dart` |
| `Applying` | 应用 | `features/cull/presentation/cull_job_runner.dart` |
| `Copying` | 复制 | `features/cull/presentation/cull_job_runner.dart` |
| `Delivered ${summary.delivered} photo(s) to ${server.name}` | 已交付 ${summary.delivered} 张照片到 ${server.name} | `features/cull/presentation/cull_job_runner.dart` |
| `Export cancelled` | 导出已取消 | `features/cull/presentation/cull_job_runner.dart` |
| `Exported ${summary.written} photo(s)` | 已导出 ${summary.written} 张照片 | `features/cull/presentation/cull_job_runner.dart` |
| `Exported ${summary.written} photo(s) · $failed failed` | 已导出 ${summary.written} 张照片 · $failed 个失败 | `features/cull/presentation/cull_job_runner.dart` |
| `Found ${result.burstCount} similar group(s), ${result.memberIds.length} photos · ${sensitivity.label} (Similar filter)` | 找到 ${result.burstCount} 个相似组、${result.memberIds.length} 张照片 · ${sensitivity.label}（相似筛选） | `features/cull/presentation/cull_job_runner.dart` |
| `Moving` | 移动 | `features/cull/presentation/cull_job_runner.dart` |
| `No gallery to upload into` | 没有可上传的画廊 | `features/cull/presentation/cull_job_runner.dart` |
| `No matching client marks in “${request.galleryName}”` | “${request.galleryName}” 中没有匹配的客户标记 | `features/cull/presentation/cull_job_runner.dart` |
| `No similar photos found (${sensitivity.label} sensitivity)` | 未找到相似照片（${sensitivity.label} 敏感度） | `features/cull/presentation/cull_job_runner.dart` |
| `Nothing was rendered to upload` | 没有可上传的渲染结果 | `features/cull/presentation/cull_job_runner.dart` |
| `Pulled ${parts.join(' + ')} from “${request.galleryName}”` | 已从“${request.galleryName}”拉取 ${parts.join(' + ')} | `features/cull/presentation/cull_job_runner.dart` |
| `Pulling` | 拉取 | `features/cull/presentation/cull_job_runner.dart` |
| `Rendering` | 渲染 | `features/cull/presentation/cull_job_runner.dart` |
| `Retry failed` | 重试失败项 | `features/cull/presentation/cull_job_runner.dart` |
| `Send cancelled` | 发送已取消 | `features/cull/presentation/cull_job_runner.dart` |
| `Sent $uploaded photo(s) to ContactSheet` | 已发送 $uploaded 张照片到 ContactSheet | `features/cull/presentation/cull_job_runner.dart` |
| `Transfer cancelled` | 传输已取消 | `features/cull/presentation/cull_job_runner.dart` |
| `Uploading` | 上传 | `features/cull/presentation/cull_job_runner.dart` |
| `$n ${n == 1 ? 'mark' : 'marks'} saved, but the .xmp sidecar couldn't be written — check the folder is writable.` | $n 条标记已保存，但 .xmp 附属文件无法写入——请检查文件夹是否可写。 | `features/cull/presentation/cull_page.dart` |
| `Error: $e` | 错误：$e | `features/cull/presentation/cull_page.dart` |
| `${failed.length} failed` | ${failed.length} 个失败 | `features/cull/presentation/cull_page.jobs.dart` |
| `${summary.failed} failed` | ${summary.failed} 个失败 | `features/cull/presentation/cull_page.jobs.dart` |
| `${summary.unchanged} unchanged` | ${summary.unchanged} 个未更改 | `features/cull/presentation/cull_page.jobs.dart` |
| `Cleared similar grouping` | 已清除相似分组 | `features/cull/presentation/cull_page.jobs.dart` |
| `Moved ${result.deleted} $noun to the Trash` | 已将 ${result.deleted} 个$noun 移到废纸篓 | `features/cull/presentation/cull_page.jobs.dart` |
| `No editors configured yet — add one in Settings` | 尚未配置编辑器——请在设置中添加 | `features/cull/presentation/cull_page.jobs.dart` |
| `No rejected photos in this folder` | 此文件夹没有已剔除照片 | `features/cull/presentation/cull_page.jobs.dart` |
| `Opening ${paths.length} photo${paths.length == 1 ? '' : 's'} in ${editor.label}` | 正在 ${editor.label} 中打开 ${paths.length} 张照片 | `features/cull/presentation/cull_page.jobs.dart` |
| `Performance set to ${changed.label} — restart Cullimingo to apply` | 性能已设为 ${changed.label}——重启 Cullimingo 后生效 | `features/cull/presentation/cull_page.jobs.dart` |
| `Renamed ${summary.renamed} photo(s)` | 已重命名 ${summary.renamed} 张照片 | `features/cull/presentation/cull_page.jobs.dart` |
| `Nothing to redo` | 没有可重做的操作 | `features/cull/presentation/cull_page.keyboard.dart` |
| `Nothing to undo` | 没有可撤销的操作 | `features/cull/presentation/cull_page.keyboard.dart` |
| `Redid $redone` | 已重做 $redone | `features/cull/presentation/cull_page.keyboard.dart` |
| `Undid $undone` | 已撤销 $undone | `features/cull/presentation/cull_page.keyboard.dart` |
| `Cullimingo ${update.version} is available.` | Cullimingo ${update.version} 已可用。 | `features/cull/presentation/cull_page.notices.dart` |
| `Download` | 下载 | `features/cull/presentation/cull_page.notices.dart` |
| ` (+$extra bracket frames)` | （另含 $extra 张包围曝光） | `features/cull/presentation/cull_page.selections.dart` |
| `$nameCount name(s) from $fileName.` | 来自 $fileName 的 $nameCount 个名称。 | `features/cull/presentation/cull_page.selections.dart` |
| `Applied marks to $n bracket frame(s)` | 已将标记应用到 $n 张包围曝光 | `features/cull/presentation/cull_page.selections.dart` |
| `Deleted "${selection.name}"` | 已删除“${selection.name}” | `features/cull/presentation/cull_page.selections.dart` |
| `Expanded ${selected.length} → ${expanded.length} photos` | 已从 ${selected.length} 张扩展到 ${expanded.length} 张 | `features/cull/presentation/cull_page.selections.dart` |
| `Find photos by filename` | 按文件名查找照片 | `features/cull/presentation/cull_page.selections.dart` |
| `Import` | 导入 | `features/cull/presentation/cull_page.selections.dart` |
| `Import selection list` | 导入选择列表 | `features/cull/presentation/cull_page.selections.dart` |
| `Loaded "${selection.name}" (${selection.photoIds.length})` | 已加载“${selection.name}”（${selection.photoIds.length} 张） | `features/cull/presentation/cull_page.selections.dart` |
| `No bracket members to add` | 没有可添加的包围曝光成员 | `features/cull/presentation/cull_page.selections.dart` |
| `Only RAWs (skip JPEG twins)` | 仅 RAW（跳过对应 JPEG） | `features/cull/presentation/cull_page.selections.dart` |
| `Paste a list of filenames (from Capture One, Lightroom or ContactSheet). Any separator works, and the extension is optional — a JPEG list still selects your RAWs.` | 粘贴文件名列表（来自 Capture One、Lightroom 或 ContactSheet）。分隔符不限，扩展名可省略——JPEG 列表同样能选中你的 RAW。 | `features/cull/presentation/cull_page.selections.dart` |
| `Save selection` | 保存选择 | `features/cull/presentation/cull_page.selections.dart` |
| `Saved "${name.trim()}" (${ids.length} photo(s))` | 已保存“${name.trim()}”（${ids.length} 张） | `features/cull/presentation/cull_page.selections.dart` |
| `Select photos first to save a selection` | 请先选择照片再保存选择 | `features/cull/presentation/cull_page.selections.dart` |
| `Selected ${ids.length} of ${list.filenames.length} from ${file.name}${_bracketSuffix(ids, selected)}` | 已从 ${file.name} 中选中 ${ids.length} / ${list.filenames.length} 张${_bracketSuffix(ids, selected)} | `features/cull/presentation/cull_page.selections.dart` |
| `Selected ${ids.length} of ${names.length} name(s)${_bracketSuffix(ids, selected)}` | 已从 ${names.length} 个名称中选中 ${ids.length} 张${_bracketSuffix(ids, selected)} | `features/cull/presentation/cull_page.selections.dart` |
| `Selection name` | 选择名称 | `features/cull/presentation/cull_page.selections.dart` |
| `Stacked $n photos` | 已堆叠 $n 张照片 | `features/cull/presentation/cull_page.selections.dart` |
| `Unstacked $n photos` | 已取消堆叠 $n 张照片 | `features/cull/presentation/cull_page.selections.dart` |
| `When a name has both a RAW and a JPEG, select just the RAW. A JPEG with no RAW twin is still selected.` | 当同一文件名同时有 RAW 和 JPEG 时，只选择 RAW。没有对应 RAW 的 JPEG 仍会被选中。 | `features/cull/presentation/cull_page.selections.dart` |
| `Import` | 导入 | `features/cull/presentation/cull_page.selections.dart、features/cull/presentation/cull_page.workspace.dart、features/cull/presentation/widgets/cull_top_bar.dart、features/ingest/presentation/ingest_dialog.dart、features/settings/presentation/settings_dialog.dart` |
| `Cancel` | 取消 | `features/cull/presentation/cull_page.selections.dart、features/cull/presentation/widgets/delete_rejects_dialog.dart、features/cull/presentation/widgets/export_bar.dart、features/cull/presentation/widgets/find_similar_dialog.dart、features/delivery/presentation/delivery_server_dialog.dart、features/export/presentation/export_dialog.dart、features/filter/presentation/filter_bar.dart、features/handoff/presentation/contactsheet_dialog.dart、features/handoff/presentation/transfer_dialog.dart、features/ingest/presentation/ingest_dialog.dart、features/metadata/presentation/code_table_dialog.dart、features/metadata/presentation/hot_codes_dialog.dart、features/metadata/presentation/iptc_editor_dialog.dart、features/metadata/presentation/iptc_template_dialog.dart、features/metadata/presentation/keyword_dialog.dart、features/naming/presentation/name_builder.dart、features/naming/presentation/rename_dialog.dart、features/settings/presentation/settings_dialog.dart、shared/widgets/dialog_kit.dart` |
| ` · ${marks.conflicts} conflict(s)` |  · ${marks.conflicts} 个冲突 | `features/cull/presentation/cull_page.workspace.dart` |
| ` · ${result.conflicts} conflict(s)` |  · ${result.conflicts} 个冲突 | `features/cull/presentation/cull_page.workspace.dart` |
| `$missing saved folder(s) no longer available` | $missing 个已保存的文件夹不再可用 | `features/cull/presentation/cull_page.workspace.dart` |
| `${marks.updated} mark(s) from disk` | 来自磁盘的 ${marks.updated} 条标记 | `features/cull/presentation/cull_page.workspace.dart` |
| `${outcome.noGps} without GPS` | ${outcome.noGps} 张无 GPS | `features/cull/presentation/cull_page.workspace.dart` |
| `${outcome.noPlace} with no place nearby` | ${outcome.noPlace} 张附近无地点 | `features/cull/presentation/cull_page.workspace.dart` |
| `${parts.isEmpty ? '' : ' · '}${scan.unreadable} item(s) couldn't be read` | ${parts.isEmpty ? '' : ' · '}${scan.unreadable} 个项目无法读取 | `features/cull/presentation/cull_page.workspace.dart` |
| `+${scan.added} / −${scan.removed} file(s)` | +${scan.added} / −${scan.removed} 个文件 | `features/cull/presentation/cull_page.workspace.dart` |
| `Applied the metadata template to ${outcome.count} photo(s)` | 已将元数据模板应用到 ${outcome.count} 张照片 | `features/cull/presentation/cull_page.workspace.dart` |
| `Can't refresh: the folder is missing or empty — is the card or drive connected? Nothing was removed.` | 无法刷新：文件夹缺失或为空——存储卡或驱动器是否已连接？未删除任何内容。 | `features/cull/presentation/cull_page.workspace.dart` |
| `Card '${card.name}' detected` | 检测到存储卡“${card.name}” | `features/cull/presentation/cull_page.workspace.dart` |
| `Filled location on ${outcome.filled} photo(s)${skipped.isEmpty ? '' : ' · $skipped'}` | 已为 ${outcome.filled} 张照片填充位置${skipped.isEmpty ? '' : ' · $skipped'} | `features/cull/presentation/cull_page.workspace.dart` |
| `Folder up to date` | 文件夹已是最新 | `features/cull/presentation/cull_page.workspace.dart` |
| `No location filled — $skipped` | 未填充位置——$skipped | `features/cull/presentation/cull_page.workspace.dart` |
| `No metadata template set up — add one in Settings` | 尚未设置元数据模板——请在设置中添加 | `features/cull/presentation/cull_page.workspace.dart` |
| `Refreshed: +${result.added} / −${result.removed} photo(s)${result.changedPaths.isEmpty ? '' : ' · '\n                          '${result.changedPaths.length} changed'}` | 已刷新：+${result.added} / −${result.removed} 张${result.changedPaths.isEmpty ? '' : ' · ${result.changedPaths.length} 张有改动'} | `features/cull/presentation/cull_page.workspace.dart` |
| `Refreshed: +${result.added} photo(s), but ${result.unreadable} item(s) in the folder couldn't be read — nothing was removed. Check the card or drive and its permissions.` | 已刷新：+${result.added} 张照片，但 ${result.unreadable} 个项目无法读取——未删除任何内容。请检查存储卡或驱动器及其权限。 | `features/cull/presentation/cull_page.workspace.dart` |
| `Select photos to apply the template to` | 请选择要应用模板的照片 | `features/cull/presentation/cull_page.workspace.dart` |
| `Select photos to fill their location from GPS` | 请选择照片以从 GPS 填充位置 | `features/cull/presentation/cull_page.workspace.dart` |
| `Sidecars already up to date` | 附属文件已是最新 | `features/cull/presentation/cull_page.workspace.dart` |
| `Stamped the metadata template onto $stamped ingested photo(s)` | 已将元数据模板盖印到 $stamped 张导入照片 | `features/cull/presentation/cull_page.workspace.dart` |
| `Synced ${parts.join(' · ')}$conflicts$unreadable` | 已同步 ${parts.join(' · ')}$conflicts$unreadable | `features/cull/presentation/cull_page.workspace.dart` |
| `The folder is no longer available (ejected or deleted)` | 文件夹已不可用（已弹出或删除） | `features/cull/presentation/cull_page.workspace.dart` |
| `Thumbnail cache cleared` | 缩略图缓存已清除 | `features/cull/presentation/cull_page.workspace.dart` |
| `Updated ${result.updated} photo(s) from disk$conflicts` | 已从磁盘更新 ${result.updated} 张照片$conflicts | `features/cull/presentation/cull_page.workspace.dart` |
| `Arrows focus · 1-5 / P / X / colours mark · ✕ drops · Esc closes` | 方向键聚焦 · 1-5 / P / X / 色标标记 · ✕ 移除 · Esc 关闭 | `features/cull/presentation/widgets/compare_view.dart` |
| `Close compare (Esc)` | 关闭对比（Esc） | `features/cull/presentation/widgets/compare_view.dart` |
| `Compare $count photos` | 对比 $count 张照片 | `features/cull/presentation/widgets/compare_view.dart` |
| `Remove from compare` | 从对比中移除 | `features/cull/presentation/widgets/compare_view.dart` |
| `Open another folder` | 打开另一个文件夹 | `features/cull/presentation/widgets/cull_tab_bar.dart` |
| `Open folder / recent` | 打开文件夹 / 最近 | `features/cull/presentation/widgets/cull_tab_bar.dart` |
| `Open folder…` | 打开文件夹… | `features/cull/presentation/widgets/cull_tab_bar.dart` |
| `${label.name} ($key)` | ${label.name}（$key） | `features/cull/presentation/widgets/cull_toolbar.dart` |
| `Edit metadata (M)` | 编辑元数据（M） | `features/cull/presentation/widgets/cull_toolbar.dart` |
| `Keywords (K)` | 关键字（K） | `features/cull/presentation/widgets/cull_toolbar.dart` |
| `Keywords: ${photo.keywords.join(', ')}` | 关键字：${photo.keywords.join(', ')} | `features/cull/presentation/widgets/cull_toolbar.dart` |
| `Pick (P)` | 精选（P） | `features/cull/presentation/widgets/cull_toolbar.dart` |
| `Rate $i` | 评 $i 星 | `features/cull/presentation/widgets/cull_toolbar.dart` |
| `Reject (X)` | 剔除（X） | `features/cull/presentation/widgets/cull_toolbar.dart` |
| `Rotate left` | 向左旋转 | `features/cull/presentation/widgets/cull_toolbar.dart` |
| `Rotate right` | 向右旋转 | `features/cull/presentation/widgets/cull_toolbar.dart` |
| `$count photos` | $count 张 | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `${selection.name} (${selection.photoIds.length})` | ${selection.name}（${selection.photoIds.length}） | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Apply marks to whole bracket` | 将标记应用到整个包围曝光 | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Apply metadata template (T)` | 应用元数据模板（T） | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Ascending` | 升序 | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Clear similar grouping` | 清除相似分组 | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Compare selected (C)` | 对比已选（C） | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Delete rejected photos… (⌘⌫)` | 删除已剔除照片…（⌘⌫） | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Descending` | 降序 | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Edit keywords (K)` | 编辑关键字（K） | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Edit metadata (M)` | 编辑元数据（M） | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Expand selection to bracket (G)` | 扩展选择到包围曝光（G） | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Fill location from GPS` | 从 GPS 填充位置 | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Find by filename (⌘F)` | 按文件名查找（⌘F） | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Find similar photos` | 查找相似照片 | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Hide info (I)` | 隐藏信息（I） | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Import selection list…` | 导入选择列表… | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Keyboard shortcuts (?)` | 键盘快捷键（?） | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Library` | 图库 | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Open folder (⌘/Ctrl O)` | 打开文件夹（⌘/Ctrl O） | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Open folder: including sub-folders` | 打开文件夹：包含子文件夹 | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Open folder: top level only` | 打开文件夹：仅顶层 | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Re-sync sidecars from disk` | 从磁盘重新同步附属文件 | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Refresh folder (⌘R)` | 刷新文件夹（⌘R） | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Save current selection…` | 保存当前选择… | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Saved selections` | 已保存选择 | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Show info (I)` | 显示信息（I） | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Sort by` | 排序方式 | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Syncing $pending…` | 正在同步 $pending… | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Writing marks to XMP sidecars` | 正在将标记写入 XMP 附属文件 | `features/cull/presentation/widgets/cull_top_bar.dart` |
| `Open folder` | 打开文件夹 | `features/cull/presentation/widgets/cull_top_bar.dart、features/cull/presentation/widgets/empty_states.dart、features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Settings` | 设置 | `features/cull/presentation/widgets/cull_top_bar.dart、features/settings/presentation/settings_dialog.dart` |
| `Delete $count photos` | 删除 $count 张照片 | `features/cull/presentation/widgets/delete_rejects_dialog.dart` |
| `Delete photo` | 删除照片 | `features/cull/presentation/widgets/delete_rejects_dialog.dart` |
| `Delete rejected photos` | 删除已剔除照片 | `features/cull/presentation/widgets/delete_rejects_dialog.dart` |
| `Move $count $descriptor to the Trash?\n\nThe originals and their .xmp sidecars leave this folder. Nothing is permanently deleted — you can restore them from the Trash.` | 将 $count $descriptor 移到废纸篓？\n\n原图及其 .xmp 附属文件将离开此文件夹。不会永久删除——可从废纸篓恢复。 | `features/cull/presentation/widgets/delete_rejects_dialog.dart` |
| `Move to Trash` | 移到废纸篓 | `features/cull/presentation/widgets/delete_rejects_dialog.dart` |
| `rejected photo` | 已剔除照片 | `features/cull/presentation/widgets/delete_rejects_dialog.dart` |
| `rejected photos` | 已剔除照片 | `features/cull/presentation/widgets/delete_rejects_dialog.dart` |
| `Clear filters` | 清除筛选 | `features/cull/presentation/widgets/empty_states.dart` |
| `No photos match the current filter` | 没有符合当前筛选的照片 | `features/cull/presentation/widgets/empty_states.dart` |
| `Open a folder of RAWs or JPEGs to start culling` | 打开 RAW 或 JPEG 文件夹开始筛选 | `features/cull/presentation/widgets/empty_states.dart` |
| `Open folder` | 打开文件夹 | `features/cull/presentation/widgets/empty_states.dart` |
| `Version $kAppVersion` | 版本 $kAppVersion | `features/cull/presentation/widgets/empty_states.dart` |
| `$verb $done of $total…` | $verb $done / $total… | `features/cull/presentation/widgets/export_bar.dart` |
| `Exporting` | 导出 | `features/cull/presentation/widgets/export_bar.dart` |
| `Find similar` | 查找相似 | `features/cull/presentation/widgets/find_similar_dialog.dart` |
| `Find similar photos` | 查找相似照片 | `features/cull/presentation/widgets/find_similar_dialog.dart` |
| `Sensitivity` | 敏感度 | `features/cull/presentation/widgets/find_similar_dialog.dart` |
| `Add to selection` | 加入选择 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Close loupe / compare` | 关闭放大视图 / 对比 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Close tab` | 关闭标签页 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Colour labels` | 色标 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Culling here is keyboard-first. The essentials to get going:` | 本应用以键盘操作为主。入门要点： | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Customize…` | 自定义… | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Delete rejected photos…` | 删除已剔除照片… | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Find by filename` | 按文件名查找 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Got it` | 知道了 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Keyboard shortcuts` | 键盘快捷键 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Loupe (also opens it)` | 放大视图（同样打开） | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Metadata editor: previous photo` | 元数据编辑器：上一张 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Metadata editor: save & next photo` | 元数据编辑器：保存并跳下一张 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Move between photos` | 在照片间移动 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Move focus` | 移动焦点 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Navigation & app` | 导航与应用 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `New tab` | 新标签页 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Open loupe / play video` | 打开放大视图 / 播放视频 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Open the loupe` | 打开放大视图 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Pick / reject` | 精选 / 剔除 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Press ? any time for the full list — and rebind anything under Settings.` | 随时按 ? 查看完整列表——所有快捷键可在设置中重新绑定。 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Previous / next photo in loupe` | 放大视图中上一张 / 下一张 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Rate 1–5 stars` | 评 1–5 星 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Rate, flag & label` | 评分、标记与色标 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Redo mark change` | 重做标记更改 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Refresh folder` | 刷新文件夹 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Select all (filtered)` | 全选（筛选结果） | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Show this list` | 显示此列表 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Undo mark change` | 撤销标记更改 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `View & select` | 查看与选择 | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Welcome to Cullimingo` | 欢迎使用 Cullimingo | `features/cull/presentation/widgets/keyboard_shortcuts_dialog.dart` |
| `Click a key to rebind it. Arrows, Esc, Enter and the ⌘/Ctrl combos stay fixed.` | 点击按键即可重新绑定。方向键、Esc、Enter 和 ⌘/Ctrl 组合键固定不变。 | `features/cull/presentation/widgets/keyboard_shortcuts_editor.dart` |
| `Customize shortcuts` | 自定义快捷键 | `features/cull/presentation/widgets/keyboard_shortcuts_editor.dart` |
| `Press a key for “${_armed!.label}” (Esc to cancel)` | 为“${_armed!.label}”按一个键（Esc 取消） | `features/cull/presentation/widgets/keyboard_shortcuts_editor.dart` |
| `Press a key…` | 按任意键… | `features/cull/presentation/widgets/keyboard_shortcuts_editor.dart` |
| `Reset to defaults` | 恢复默认 | `features/cull/presentation/widgets/keyboard_shortcuts_editor.dart` |
| `“${keyDisplayLabel(key)}” is already used by “${clash.label}”.` | “${keyDisplayLabel(key)}”已被“${clash.label}”使用。 | `features/cull/presentation/widgets/keyboard_shortcuts_editor.dart` |
| `“${keyDisplayLabel(key)}” is reserved for navigation and can’t be assigned.` | “${keyDisplayLabel(key)}”保留给导航，无法分配。 | `features/cull/presentation/widgets/keyboard_shortcuts_editor.dart` |
| `Analysis overlays` | 分析叠加层 | `features/cull/presentation/widgets/loupe_view.dart` |
| `Can’t display this file` | 无法显示此文件 | `features/cull/presentation/widgets/loupe_view.dart` |
| `Clipping warnings` | 过曝警告 | `features/cull/presentation/widgets/loupe_view.dart` |
| `Close loupe (Esc)` | 关闭放大视图（Esc） | `features/cull/presentation/widgets/loupe_view.dart` |
| `Colour cleared` | 已清除色标 | `features/cull/presentation/widgets/loupe_view.dart` |
| `Flag cleared` | 已清除标记 | `features/cull/presentation/widgets/loupe_view.dart` |
| `Focus peaking` | 峰值对焦 | `features/cull/presentation/widgets/loupe_view.dart` |
| `Hide crop outline` | 隐藏裁剪框 | `features/cull/presentation/widgets/loupe_view.dart` |
| `Hide filmstrip` | 隐藏胶片条 | `features/cull/presentation/widgets/loupe_view.dart` |
| `Hide info (I)` | 隐藏信息（I） | `features/cull/presentation/widgets/loupe_view.dart` |
| `Histogram` | 直方图 | `features/cull/presentation/widgets/loupe_view.dart` |
| `No rating` | 无星级 | `features/cull/presentation/widgets/loupe_view.dart` |
| `Open in system player` | 在系统播放器中打开 | `features/cull/presentation/widgets/loupe_view.dart` |
| `Pick` | 已精选 | `features/cull/presentation/widgets/loupe_view.dart` |
| `Rejected` | 已剔除 | `features/cull/presentation/widgets/loupe_view.dart` |
| `Show crop outline` | 显示裁剪框 | `features/cull/presentation/widgets/loupe_view.dart` |
| `Show filmstrip` | 显示胶片条 | `features/cull/presentation/widgets/loupe_view.dart` |
| `Show info (I)` | 显示信息（I） | `features/cull/presentation/widgets/loupe_view.dart` |
| `Dismiss` | 关闭 | `features/cull/presentation/widgets/notice_bar.dart` |
| `Cropped in Lightroom / Camera Raw` | 在 Lightroom / Camera Raw 中裁剪过 | `features/cull/presentation/widgets/photo_cell.dart` |
| `Edit metadata` | 编辑元数据 | `features/cull/presentation/widgets/photo_cell.dart` |
| `Rotate left` | 向左旋转 | `features/cull/presentation/widgets/photo_cell.dart` |
| `Rotate right` | 向右旋转 | `features/cull/presentation/widgets/photo_cell.dart` |
| `Sidecar changed outside Cullimingo (resolved newest-wins)` | 附属文件在 Cullimingo 外被修改（按最新内容解决） | `features/cull/presentation/widgets/photo_cell.dart` |
| ` · $selectedCount selected` |  · 已选 $selectedCount 张 | `features/cull/presentation/widgets/status_bar.dart` |
| `$filteredCount of $total photos` | $total 张中的 $filteredCount 张 | `features/cull/presentation/widgets/status_bar.dart` |
| `$total photo${total == 1 ? '' : 's'}` | $total 张照片 | `features/cull/presentation/widgets/status_bar.dart` |
| `Export $n photo${n == 1 ? '' : 's'}` | 导出 $n 张照片 | `features/cull/presentation/widgets/status_bar.dart` |
| `Export $n selected` | 导出已选 $n 张 | `features/cull/presentation/widgets/status_bar.dart` |
| `Export (⌘/Ctrl S)` | 导出（⌘/Ctrl S） | `features/cull/presentation/widgets/status_bar.dart` |
| `$count photos` | $count 张照片 | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Apply marks to bracket` | 应用标记到包围曝光 | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Apply metadata template` | 应用元数据模板 | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Copy to folder…` | 复制到文件夹… | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Delete…` | 删除… | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Edit keywords…` | 编辑关键字… | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Edit metadata…` | 编辑元数据… | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Expand selection to bracket` | 扩展选择到包围曝光 | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Export…` | 导出… | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Fill location from GPS` | 从 GPS 填充位置 | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Move to folder…` | 移动到文件夹… | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Open in ${editor.label}` | 在 ${editor.label} 中打开 | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Open in default app` | 在默认应用中打开 | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Pull marks from ContactSheet…` | 从 ContactSheet 拉取标记… | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Remove from bracket` | 从包围曝光中移除 | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Rename…` | 重命名… | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Rotate left` | 向左旋转 | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Rotate right` | 向右旋转 | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Send to ContactSheet…` | 发送到 ContactSheet… | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `Stack as bracket` | 堆叠为包围曝光 | `features/cull/presentation/widgets/thumbnail_context_menu.dart` |
| `$host closed the connection` | $host 已关闭连接 | `features/delivery/data/ftp_client.dart` |
| `$host did not answer within ${timeout.inSeconds}s` | $host 在 ${timeout.inSeconds} 秒内未响应 | `features/delivery/data/ftp_client.dart` |
| `$host refused $step` | $host 拒绝了 $step | `features/delivery/data/ftp_client.dart` |
| `Connection to $host — $error` | 到 $host 的连接——$error | `features/delivery/data/ftp_client.dart` |
| `Could not connect to $host:$port — $e` | 无法连接 $host:$port——$e | `features/delivery/data/ftp_client.dart` |
| `Could not create "$segment" on $host` | 无法在 $host 上创建“$segment” | `features/delivery/data/ftp_client.dart` |
| `Could not parse the passive-mode reply from $host` | 无法解析来自 $host 的被动模式回复 | `features/delivery/data/ftp_client.dart` |
| `Data connection to $host:$dataPort failed — $e` | 到 $host:$dataPort 的数据连接失败——$e | `features/delivery/data/ftp_client.dart` |
| `Malformed reply from $host: "$first"` | 来自 $host 的异常回复：“$first” | `features/delivery/data/ftp_client.dart` |
| `Server refused upload of "$remoteName"` | 服务器拒绝了“$remoteName”的上传 | `features/delivery/data/ftp_client.dart` |
| `TLS handshake with $host failed — $e` | 与 $host 的 TLS 握手失败——$e | `features/delivery/data/ftp_client.dart` |
| `transfer of $remoteName` | 传输 $remoteName | `features/delivery/data/ftp_client.dart` |
| `$host refused the login for "$username"` | $host 拒绝了用户“$username”的登录 | `features/delivery/data/sftp_client.dart` |
| `Could not connect to $host:$port — $e` | 无法连接 $host:$port——$e | `features/delivery/data/sftp_client.dart` |
| `Could not create "$path" on $host` | 无法在 $host 上创建“$path” | `features/delivery/data/sftp_client.dart` |
| `Could not read the key "$keyFilePath" — $e` | 无法读取密钥“$keyFilePath”——$e | `features/delivery/data/sftp_client.dart` |
| `Not connected` | 未连接 | `features/delivery/data/sftp_client.dart` |
| `Upload of "$remoteName" to $host failed — $e` | “$remoteName”上传到 $host 失败——$e | `features/delivery/data/sftp_client.dart` |
| `FTPS (explicit TLS)` | FTPS（显式 TLS） | `features/delivery/domain/delivery_server.dart` |
| `Accept self-signed certificate` | 接受自签名证书 | `features/delivery/presentation/delivery_server_dialog.dart` |
| `Add server` | 添加服务器 | `features/delivery/presentation/delivery_server_dialog.dart` |
| `Choose key file` | 选择密钥文件 | `features/delivery/presentation/delivery_server_dialog.dart` |
| `Connection OK — logged in, folder reachable.` | 连接正常——已登录，文件夹可访问。 | `features/delivery/presentation/delivery_server_dialog.dart` |
| `Edit server` | 编辑服务器 | `features/delivery/presentation/delivery_server_dialog.dart` |
| `Key passphrase (empty = unencrypted key)` | 密钥口令（留空 = 密钥未加密） | `features/delivery/presentation/delivery_server_dialog.dart` |
| `Name (e.g. AP wire)` | 名称（如 AP 通讯社） | `features/delivery/presentation/delivery_server_dialog.dart` |
| `Password` | 密码 | `features/delivery/presentation/delivery_server_dialog.dart` |
| `Plain FTP sends the password unencrypted — fine on a LAN/VPN, avoid on the open internet.` | 明文 FTP 会未加密地传输密码——在局域网/专用网络中可用，公开互联网上请勿使用。 | `features/delivery/presentation/delivery_server_dialog.dart` |
| `Private key file (empty = password auth)` | 私钥文件（留空 = 密码认证） | `features/delivery/presentation/delivery_server_dialog.dart` |
| `Remote folder (e.g. incoming/photos)` | 远程文件夹（如 incoming/photos） | `features/delivery/presentation/delivery_server_dialog.dart` |
| `Test connection` | 测试连接 | `features/delivery/presentation/delivery_server_dialog.dart` |
| `Username (empty = anonymous)` | 用户名（留空 = 匿名） | `features/delivery/presentation/delivery_server_dialog.dart` |
| `Also keep a local copy` | 同时保留本地副本 | `features/export/presentation/export_dialog.dart` |
| `Choose a folder…` | 选择文件夹… | `features/export/presentation/export_dialog.dart` |
| `Custom…` | 自定义… | `features/export/presentation/export_dialog.dart` |
| `Embedded-preview export — the in-camera look (great for proofs/web), not a Capture One / Lightroom render.` | 嵌入式预览导出——机内观感（适合样片/网络），不是 Capture One / Lightroom 的渲染结果。 | `features/export/presentation/export_dialog.dart` |
| `Export $count photo${count == 1 ? '' : 's'}` | 导出 $count 张照片 | `features/export/presentation/export_dialog.dart` |
| `Export ${widget.sources.length}` | 导出 ${widget.sources.length} 张 | `features/export/presentation/export_dialog.dart` |
| `Export & upload ${widget.sources.length}` | 导出并上传 ${widget.sources.length} 张 | `features/export/presentation/export_dialog.dart` |
| `Exports` | 导出 | `features/export/presentation/export_dialog.dart` |
| `Exports (blank = alongside)` | 导出位置（留空 = 与原文件同目录） | `features/export/presentation/export_dialog.dart` |
| `Format` | 格式 | `features/export/presentation/export_dialog.dart` |
| `Limit file size to` | 限制文件大小为 | `features/export/presentation/export_dialog.dart` |
| `Local folder` | 本地文件夹 | `features/export/presentation/export_dialog.dart` |
| `Long edge` | 长边 | `features/export/presentation/export_dialog.dart` |
| `Open folder when done` | 完成后打开文件夹 | `features/export/presentation/export_dialog.dart` |
| `Original` | 原始 | `features/export/presentation/export_dialog.dart` |
| `Output` | 输出 | `features/export/presentation/export_dialog.dart` |
| `Same folder as originals` | 与原文件同文件夹 | `features/export/presentation/export_dialog.dart` |
| `Sharpen after resize` | 缩放后锐化 | `features/export/presentation/export_dialog.dart` |
| `Size & quality` | 尺寸与质量 | `features/export/presentation/export_dialog.dart` |
| `Subfolder` | 子文件夹 | `features/export/presentation/export_dialog.dart` |
| `Upload to ${server.name} (${server.protocol.label})` | 上传到 ${server.name}（${server.protocol.label}） | `features/export/presentation/export_dialog.dart` |
| `e.g.  $_previewName` | 例如  $_previewName | `features/export/presentation/export_dialog.dart` |
| `Quality` | 质量 | `features/export/presentation/export_dialog.dart、features/handoff/presentation/contactsheet_dialog.dart` |
| `Destination` | 目标位置 | `features/export/presentation/export_dialog.dart、features/handoff/presentation/transfer_dialog.dart、features/ingest/presentation/ingest_dialog.dart` |
| `Naming` | 命名 | `features/export/presentation/export_dialog.dart、features/ingest/presentation/ingest_dialog.dart` |
| `Capture Time` | 拍摄时间 | `features/filter/domain/photo_sort.dart` |
| `Color Class` | 色标类别 | `features/filter/domain/photo_sort.dart` |
| `Height` | 高度 | `features/filter/domain/photo_sort.dart` |
| `Lens` | 镜头 | `features/filter/domain/photo_sort.dart` |
| `Modification Time` | 修改时间 | `features/filter/domain/photo_sort.dart` |
| `Rating` | 星级 | `features/filter/domain/photo_sort.dart` |
| `Width` | 宽度 | `features/filter/domain/photo_sort.dart` |
| `Captured` | 拍摄时间 | `features/filter/domain/photo_sort.dart、features/inspector/presentation/inspector_panel.dart` |
| `Camera` | 相机 | `features/filter/domain/photo_sort.dart、features/inspector/presentation/inspector_panel.dart、features/naming/domain/name_element.dart` |
| `Filename` | 文件名 | `features/filter/domain/photo_sort.dart、features/naming/presentation/name_builder.dart` |
| `$groupLabel ($groupCount)` | $groupLabel（$groupCount） | `features/filter/presentation/filter_bar.dart` |
| `${label.displayName} label — showing only these` | 只看 ${label.displayName} 色标 | `features/filter/presentation/filter_bar.dart` |
| `All (${all.length})` | 全部（${all.length}） | `features/filter/presentation/filter_bar.dart` |
| `All file types` | 全部文件类型 | `features/filter/presentation/filter_bar.dart` |
| `Bursts` | 连拍 | `features/filter/presentation/filter_bar.dart` |
| `Filter presets` | 筛选预设 | `features/filter/presentation/filter_bar.dart` |
| `Filter: ${label.displayName} label` | 筛选：${label.displayName} 色标 | `features/filter/presentation/filter_bar.dart` |
| `Grouping` | 分组 | `features/filter/presentation/filter_bar.dart` |
| `Hide JPEG ($pairCount)` | 隐藏 JPEG（$pairCount） | `features/filter/presentation/filter_bar.dart` |
| `JPEG only ($jpegCount)` | 仅 JPEG（$jpegCount） | `features/filter/presentation/filter_bar.dart` |
| `Keyworded (${count((p) => p.keywords.isNotEmpty)})` | 已加关键字（${count((p) => p.keywords.isNotEmpty)}） | `features/filter/presentation/filter_bar.dart` |
| `Needs caption (${count((p) => p.iptc.caption.trim().isEmpty)})` | 缺说明（${count((p) => p.iptc.caption.trim().isEmpty)}） | `features/filter/presentation/filter_bar.dart` |
| `Picks (${count((p) => p.flag == PickFlag.pick)})` | 精选（${count((p) => p.flag == PickFlag.pick)}） | `features/filter/presentation/filter_bar.dart` |
| `Preset name` | 预设名称 | `features/filter/presentation/filter_bar.dart` |
| `RAW only ($rawCount)` | 仅 RAW（$rawCount） | `features/filter/presentation/filter_bar.dart` |
| `Rating ≥ $star` | 星级 ≥ $star | `features/filter/presentation/filter_bar.dart` |
| `Rejected (${count((p) => p.flag == PickFlag.reject)})` | 已剔除（${count((p) => p.flag == PickFlag.reject)}） | `features/filter/presentation/filter_bar.dart` |
| `Save current filter…` | 保存当前筛选… | `features/filter/presentation/filter_bar.dart` |
| `Save filter preset` | 保存筛选预设 | `features/filter/presentation/filter_bar.dart` |
| `Search filename…` | 搜索文件名… | `features/filter/presentation/filter_bar.dart` |
| `Selected ($selectedCount)` | 已选（$selectedCount） | `features/filter/presentation/filter_bar.dart` |
| `Similar` | 相似 | `features/filter/presentation/filter_bar.dart` |
| `Stack brackets ($bracketCount)` | 堆叠包围曝光（$bracketCount） | `features/filter/presentation/filter_bar.dart` |
| `Metadata` | 元数据 | `features/filter/presentation/filter_bar.dart、features/metadata/presentation/iptc_editor_dialog.dart、features/settings/presentation/settings_dialog.dart` |
| `Could not reach ContactSheet ($e)` | 无法连接 ContactSheet（$e） | `features/handoff/data/contactsheet_client.dart` |
| `Not authorised — check the token and its scopes` | 未授权——请检查令牌及其权限范围 | `features/handoff/data/contactsheet_client.dart` |
| `Not found — check the URL or gallery` | 未找到——请检查 URL 或画廊 | `features/handoff/data/contactsheet_client.dart` |
| `Server returned ${res.statusCode}` | 服务器返回 ${res.statusCode} | `features/handoff/data/contactsheet_client.dart` |
| `Photo copied, but its sidecar wasn't: ${sidecarResult.message ?? sidecarResult.outcome.name}` | 照片已复制，但其附属文件未复制：${sidecarResult.message ?? sidecarResult.outcome.name} | `features/handoff/data/transfer_service.dart` |
| `${flattenGalleryTree(_galleries!).length} galleries` | ${flattenGalleryTree(_galleries!).length} 个画廊 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Access token (cs_pat_…)` | 访问令牌（cs_pat_…） | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Change` | 更换 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Create a new gallery, or load existing ones.` | 创建新画廊，或加载已有画廊。 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Fetches client ratings + colours and applies them to the matching photos by filename (selecting the ones the client marked).` | 按文件名拉取客户评分 + 色标并应用到匹配的照片（即客户标记的那些）。 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Gallery` | 画廊 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Import collections as saved selections` | 将收藏导入为已保存选择 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Load existing` | 加载已有 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Load the gallery the client reviewed.` | 加载客户浏览过的画廊。 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Loading…` | 正在加载… | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Long edge` | 长边 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Nested sub-gallery` | 嵌套子画廊 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `New gallery name` | 新画廊名称 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `New gallery name…` | 新画廊名称… | `features/handoff/presentation/contactsheet_dialog.dart` |
| `New gallery…` | 新建画廊… | `features/handoff/presentation/contactsheet_dialog.dart` |
| `New sub-gallery` | 新建子画廊 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `No galleries match.` | 没有匹配的画廊。 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Pull marks` | 拉取标记 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Reload` | 重新加载 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Renders JPEGs (in-camera look) and uploads them to the gallery.` | 渲染 JPEG（机内观感）并上传到画廊。 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Search galleries…` | 搜索画廊… | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Send $count` | 发送 $count | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Server` | 服务器 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Size & quality` | 尺寸与质量 | `features/handoff/presentation/contactsheet_dialog.dart` |
| `Remove` | 移除 | `features/handoff/presentation/contactsheet_dialog.dart、features/metadata/presentation/code_table_dialog.dart、features/settings/presentation/settings_dialog.dart` |
| `$verb $count photo${count == 1 ? '' : 's'}` | $verb $count 张照片 | `features/handoff/presentation/transfer_dialog.dart` |
| `$verb ${widget.sources.length}` | $verb ${widget.sources.length} 张 | `features/handoff/presentation/transfer_dialog.dart` |
| `Choose a folder…` | 选择文件夹… | `features/handoff/presentation/transfer_dialog.dart` |
| `Copy` | 复制 | `features/handoff/presentation/transfer_dialog.dart` |
| `Copy duplicates the originals; the files stay where they are.` | 复制会生成原文件的副本；原文件保留在原处。 | `features/handoff/presentation/transfer_dialog.dart` |
| `Include XMP sidecars` | 包含 XMP 附属文件 | `features/handoff/presentation/transfer_dialog.dart` |
| `Move` | 移动 | `features/handoff/presentation/transfer_dialog.dart` |
| `Move copies the originals to the destination and removes them from their current folder — only after each copy is verified.` | 移动会把原文件复制到目标位置，并在每次复制校验通过后才将其从当前文件夹移除。 | `features/handoff/presentation/transfer_dialog.dart` |
| `Open folder when done` | 完成后打开文件夹 | `features/handoff/presentation/transfer_dialog.dart` |
| `Subfolder (optional, e.g. selects)` | 子文件夹（可选，如 selects） | `features/handoff/presentation/transfer_dialog.dart` |
| `$n ${n == 1 ? 'item' : 'items'} on the source couldn't be read and won't be imported. Don't format the card until you've checked it.` | 来源上的 $n 个项目无法读取，不会被导入。确认检查完成前请勿格式化存储卡。 | `features/ingest/presentation/ingest_dialog.dart` |
| `${_dayMonths[d.month - 1]} ${d.day}` | ${d.month}月${d.day}日 | `features/ingest/presentation/ingest_dialog.dart` |
| `${plan.items.length} photos · ${_formatBytes(plan.totalBytes)}` | ${plan.items.length} 张照片 · ${_formatBytes(plan.totalBytes)} | `features/ingest/presentation/ingest_dialog.dart` |
| `${v.name}  •  card` | ${v.name} • 存储卡 | `features/ingest/presentation/ingest_dialog.dart` |
| `Already present (skipped)` | 已存在（已跳过） | `features/ingest/presentation/ingest_dialog.dart` |
| `Also copy to a backup destination (always verified)` | 同时复制到备份目标（始终校验） | `features/ingest/presentation/ingest_dialog.dart` |
| `Browse…` | 浏览… | `features/ingest/presentation/ingest_dialog.dart` |
| `Cancelling…` | 正在取消… | `features/ingest/presentation/ingest_dialog.dart` |
| `Checking destinations…` | 正在检查目标… | `features/ingest/presentation/ingest_dialog.dart` |
| `Choose a destination to import` | 选择导入目标位置 | `features/ingest/presentation/ingest_dialog.dart` |
| `Choose backup…` | 选择备份位置… | `features/ingest/presentation/ingest_dialog.dart` |
| `Choose the backup destination` | 选择备份目标位置 | `features/ingest/presentation/ingest_dialog.dart` |
| `Choose where the photos are copied…` | 选择照片复制目标… | `features/ingest/presentation/ingest_dialog.dart` |
| `Conflicts (kept existing)` | 冲突（保留现有文件） | `features/ingest/presentation/ingest_dialog.dart` |
| `Copied & verified` | 已复制并校验 | `features/ingest/presentation/ingest_dialog.dart` |
| `Copied (not verified)` | 已复制（未校验） | `features/ingest/presentation/ingest_dialog.dart` |
| `Copied (only the backup verified)` | 已复制（仅备份已校验） | `features/ingest/presentation/ingest_dialog.dart` |
| `Copying ${pr.done} / ${pr.total}  ·  ${_speed(pr)}  —  ${p.basename(pr.last.source)}` | 正在复制 ${pr.done} / ${pr.total} · ${_speed(pr)} — ${p.basename(pr.last.source)} | `features/ingest/presentation/ingest_dialog.dart` |
| `Couldn't read on the source` | 在来源上无法读取 | `features/ingest/presentation/ingest_dialog.dart` |
| `Couldn't scan this source: $_scanError` | 无法扫描此来源：$_scanError | `features/ingest/presentation/ingest_dialog.dart` |
| `Days on this card — $included of ${counts.length} included` | 此卡上的日期——已包含 $included / ${counts.length} 天 | `features/ingest/presentation/ingest_dialog.dart` |
| `Everything is filtered out — re-include a day or file type.` | 全部已被筛选排除——请重新包含某个日期或文件类型。 | `features/ingest/presentation/ingest_dialog.dart` |
| `Failed` | 失败 | `features/ingest/presentation/ingest_dialog.dart` |
| `Import $count photo${count == 1 ? '' : 's'}` | 导入 $count 张照片 | `features/ingest/presentation/ingest_dialog.dart` |
| `Import cancelled` | 导入已取消 | `features/ingest/presentation/ingest_dialog.dart` |
| `Import complete` | 导入完成 | `features/ingest/presentation/ingest_dialog.dart` |
| `Import finished with issues` | 导入完成但有问题 | `features/ingest/presentation/ingest_dialog.dart` |
| `Import photos` | 导入照片 | `features/ingest/presentation/ingest_dialog.dart` |
| `Importing…` | 正在导入… | `features/ingest/presentation/ingest_dialog.dart` |
| `Include JPEGs` | 包含 JPEG | `features/ingest/presentation/ingest_dialog.dart` |
| `Include videos` | 包含视频 | `features/ingest/presentation/ingest_dialog.dart` |
| `Newest day` | 最新一天 | `features/ingest/presentation/ingest_dialog.dart` |
| `No photos found in the source.` | 来源中未找到照片。 | `features/ingest/presentation/ingest_dialog.dart` |
| `Not copied (cancelled)` | 未复制（已取消） | `features/ingest/presentation/ingest_dialog.dart` |
| `Open in library` | 在图库中打开 | `features/ingest/presentation/ingest_dialog.dart` |
| `Part of the source couldn't be read, so its files weren't imported. Don't format the card until you've checked it.` | 部分来源无法读取，其中的文件未被导入。确认检查完成前请勿格式化存储卡。 | `features/ingest/presentation/ingest_dialog.dart` |
| `Scanning…` | 正在扫描… | `features/ingest/presentation/ingest_dialog.dart` |
| `Select a card or folder` | 选择存储卡或文件夹 | `features/ingest/presentation/ingest_dialog.dart` |
| `Select a card or folder to scan.` | 选择要扫描的存储卡或文件夹。 | `features/ingest/presentation/ingest_dialog.dart` |
| `Select a source above` | 请在上方选择来源 | `features/ingest/presentation/ingest_dialog.dart` |
| `Source` | 来源 | `features/ingest/presentation/ingest_dialog.dart` |
| `Starting…` | 正在开始… | `features/ingest/presentation/ingest_dialog.dart` |
| `Still being written (import again)` | 仍在写入（请重新导入） | `features/ingest/presentation/ingest_dialog.dart` |
| `That looks like a whole drive. Choose a folder on it with Browse… (or insert a camera card) to scan.` | 这看起来是整个驱动器。用「浏览…」选择其中的一个文件夹（或插入相机存储卡）以扫描。 | `features/ingest/presentation/ingest_dialog.dart` |
| `Today · $date` | 今天 · $date | `features/ingest/presentation/ingest_dialog.dart` |
| `Uncheck to import RAW files only` | 取消勾选则仅导入 RAW 文件 | `features/ingest/presentation/ingest_dialog.dart` |
| `Verify each copy by checksum (recommended)` | 通过校验和验证每次复制（推荐） | `features/ingest/presentation/ingest_dialog.dart` |
| `Videos are copied alongside the photos` | 视频将随照片一起复制 | `features/ingest/presentation/ingest_dialog.dart` |
| `Yesterday · $date` | 昨天 · $date | `features/ingest/presentation/ingest_dialog.dart` |
| `• ${p.basename(r.source)}: ${r.message ?? r.outcome.name}` | • ${p.basename(r.source)}：${r.message ?? r.outcome.name} | `features/ingest/presentation/ingest_dialog.dart` |
| `• ${shown(u.path)}: ${u.reason}` | • ${shown(u.path)}：${u.reason} | `features/ingest/presentation/ingest_dialog.dart` |
| `• …and ${problems.length - 5} more` | • …以及另外 ${problems.length - 5} 个 | `features/ingest/presentation/ingest_dialog.dart` |
| `Source` | 来源 | `features/ingest/presentation/ingest_dialog.dart、features/metadata/data/xmp_codec.dart、features/metadata/data/xmp_merge.dart、features/metadata/domain/iptc_core.dart、features/metadata/presentation/iptc_editor_dialog.dart、features/metadata/presentation/iptc_template_dialog.dart` |
| `Mirrored` | 镜像 | `features/inspector/domain/exif_format.dart` |
| `Mirrored, 180°` | 镜像，180° | `features/inspector/domain/exif_format.dart` |
| `Mirrored, 90° CCW` | 镜像，逆时针 90° | `features/inspector/domain/exif_format.dart` |
| `Mirrored, 90° CW` | 镜像，顺时针 90° | `features/inspector/domain/exif_format.dart` |
| `Normal` | 正常 | `features/inspector/domain/exif_format.dart` |
| `Rotated 180°` | 旋转 180° | `features/inspector/domain/exif_format.dart` |
| `Rotated 90° CCW` | 逆时针旋转 90° | `features/inspector/domain/exif_format.dart` |
| `Rotated 90° CW` | 顺时针旋转 90° | `features/inspector/domain/exif_format.dart` |
| `+ Add field` | 添加字段 | `features/inspector/presentation/inspector_panel.dart` |
| `Add a metadata field` | 添加元数据字段 | `features/inspector/presentation/inspector_panel.dart` |
| `Aperture` | 光圈 | `features/inspector/presentation/inspector_panel.dart` |
| `Artwork or object` | 艺术品或对象 | `features/inspector/presentation/inspector_panel.dart` |
| `Camera` | 相机 | `features/inspector/presentation/inspector_panel.dart` |
| `Captured` | 拍摄时间 | `features/inspector/presentation/inspector_panel.dart` |
| `Copyright owners` | 版权所有者 | `features/inspector/presentation/inspector_panel.dart` |
| `Cropped (LR) · ${formatCrop(d.crop!.width, d.crop!.height, d.crop!.angle)}` | 已在 LR 中裁剪 · ${formatCrop(d.crop!.width, d.crop!.height, d.crop!.angle)} | `features/inspector/presentation/inspector_panel.dart` |
| `Dimensions` | 尺寸 | `features/inspector/presentation/inspector_panel.dart` |
| `Exp. comp.` | 曝光补偿 | `features/inspector/presentation/inspector_panel.dart` |
| `Exposure` | 曝光 | `features/inspector/presentation/inspector_panel.dart` |
| `Focal length` | 焦距 | `features/inspector/presentation/inspector_panel.dart` |
| `Hide inspector (I)` | 隐藏检查器（I） | `features/inspector/presentation/inspector_panel.dart` |
| `Image creators` | 图像创作者 | `features/inspector/presentation/inspector_panel.dart` |
| `Licensors` | 许可方 | `features/inspector/presentation/inspector_panel.dart` |
| `Locations shown` | 所示地点 | `features/inspector/presentation/inspector_panel.dart` |
| `No caption or credit` | 无说明或署名 | `features/inspector/presentation/inspector_panel.dart` |
| `No marks` | 无标记 | `features/inspector/presentation/inspector_panel.dart` |
| `No photo selected` | 未选择照片 | `features/inspector/presentation/inspector_panel.dart` |
| `Orientation` | 方向 | `features/inspector/presentation/inspector_panel.dart` |
| `Registry entries` | 注册条目 | `features/inspector/presentation/inspector_panel.dart` |
| `Resolution` | 分辨率 | `features/inspector/presentation/inspector_panel.dart` |
| `Orientation` | 方向 | `features/inspector/presentation/inspector_panel.dart、features/metadata/data/xmp_codec.dart、features/metadata/data/xmp_merge.dart` |
| `listing stalled (device unresponsive)` | 列表读取停滞（设备无响应） | `features/library/data/folder_scanner.dart` |
| `stat stalled (device unresponsive)` | 属性读取停滞（设备无响应） | `features/library/data/folder_scanner.dart` |
| `The file could not be opened. Check that it still exists and is readable.` | 无法打开该文件。请检查它是否仍存在且可读。 | `features/metadata/data/template_file.dart` |
| `The file could not be written. Check that the folder exists and is writable.` | 无法写入该文件。请检查文件夹是否存在且可写。 | `features/metadata/data/template_file.dart` |
| `This XMP file contains no template fields — nothing to load.` | 此 XMP 文件不包含模板字段——没有可加载的内容。 | `features/metadata/data/template_file.dart` |
| `This is not an XMP template. Choose a .xmp file saved from a metadata template — by Photo Mechanic, Adobe Bridge, or Cullimingo.` | 这不是 XMP 模板。请选择由元数据模板保存的 .xmp 文件——来自 Photo Mechanic、Adobe Bridge 或 Cullimingo。 | `features/metadata/data/template_file.dart` |
| `AI & provenance` | AI 与来源信息 | `features/metadata/domain/iptc_core.dart` |
| `AI prompt` | AI 提示词 | `features/metadata/domain/iptc_core.dart` |
| `AI prompt writer` | AI 提示词作者 | `features/metadata/domain/iptc_core.dart` |
| `AI system` | AI 系统 | `features/metadata/domain/iptc_core.dart` |
| `AI system version` | AI 系统版本 | `features/metadata/domain/iptc_core.dart` |
| `Additional model info` | 模特补充信息 | `features/metadata/domain/iptc_core.dart` |
| `Alt text` | 替代文本 | `features/metadata/domain/iptc_core.dart` |
| `Caption` | 说明文字 | `features/metadata/domain/iptc_core.dart` |
| `Category` | 类别 | `features/metadata/domain/iptc_core.dart` |
| `City` | 城市 | `features/metadata/domain/iptc_core.dart` |
| `Copyright` | 版权 | `features/metadata/domain/iptc_core.dart` |
| `Copyright status` | 版权状态 | `features/metadata/domain/iptc_core.dart` |
| `Country` | 国家 | `features/metadata/domain/iptc_core.dart` |
| `Creator` | 创作者 | `features/metadata/domain/iptc_core.dart` |
| `Creator address` | 创作者地址 | `features/metadata/domain/iptc_core.dart` |
| `Creator city` | 创作者城市 | `features/metadata/domain/iptc_core.dart` |
| `Creator country` | 创作者国家 | `features/metadata/domain/iptc_core.dart` |
| `Creator email` | 创作者邮箱 | `features/metadata/domain/iptc_core.dart` |
| `Creator phone` | 创作者电话 | `features/metadata/domain/iptc_core.dart` |
| `Creator postcode` | 创作者邮编 | `features/metadata/domain/iptc_core.dart` |
| `Creator state/region` | 创作者省州 | `features/metadata/domain/iptc_core.dart` |
| `Creator website` | 创作者网站 | `features/metadata/domain/iptc_core.dart` |
| `Credit` | 署名 | `features/metadata/domain/iptc_core.dart` |
| `Credit & rights` | 署名与权利 | `features/metadata/domain/iptc_core.dart` |
| `Date created` | 创建日期 | `features/metadata/domain/iptc_core.dart` |
| `Description` | 说明 | `features/metadata/domain/iptc_core.dart` |
| `Description writers` | 说明撰写者 | `features/metadata/domain/iptc_core.dart` |
| `Edit status` | 编辑状态 | `features/metadata/domain/iptc_core.dart` |
| `Event` | 事件 | `features/metadata/domain/iptc_core.dart` |
| `Featured org` | 画面机构 | `features/metadata/domain/iptc_core.dart` |
| `Featured org code` | 画面机构代码 | `features/metadata/domain/iptc_core.dart` |
| `Headline` | 标题 | `features/metadata/domain/iptc_core.dart` |
| `IPTC scene` | IPTC 场景 | `features/metadata/domain/iptc_core.dart` |
| `ISO code` | ISO 代码 | `features/metadata/domain/iptc_core.dart` |
| `Image GUID` | 图像 GUID | `features/metadata/domain/iptc_core.dart` |
| `Image supplier` | 图像供稿方 | `features/metadata/domain/iptc_core.dart` |
| `Instructions` | 使用说明 | `features/metadata/domain/iptc_core.dart` |
| `Intellectual genre` | 题材类型 | `features/metadata/domain/iptc_core.dart` |
| `Job ID / Transmission` | 任务 ID / 传输 | `features/metadata/domain/iptc_core.dart` |
| `Job title` | 职务 | `features/metadata/domain/iptc_core.dart` |
| `Location` | 地点 | `features/metadata/domain/iptc_core.dart` |
| `Location ID` | 地点 ID | `features/metadata/domain/iptc_core.dart` |
| `Media topics` | 媒体主题 | `features/metadata/domain/iptc_core.dart` |
| `Minor model age disclosure` | 未成年模特年龄披露 | `features/metadata/domain/iptc_core.dart` |
| `Model age` | 模特年龄 | `features/metadata/domain/iptc_core.dart` |
| `Model release` | 模特授权 | `features/metadata/domain/iptc_core.dart` |
| `Model release IDs` | 模特授权 ID | `features/metadata/domain/iptc_core.dart` |
| `Models & releases` | 模特与授权 | `features/metadata/domain/iptc_core.dart` |
| `Persons shown` | 画面人物 | `features/metadata/domain/iptc_core.dart` |
| `Property release` | 财产授权 | `features/metadata/domain/iptc_core.dart` |
| `Property release IDs` | 财产授权 ID | `features/metadata/domain/iptc_core.dart` |
| `Rights URL` | 权利 URL | `features/metadata/domain/iptc_core.dart` |
| `Source type` | 来源类型 | `features/metadata/domain/iptc_core.dart` |
| `State / Province` | 省州 | `features/metadata/domain/iptc_core.dart` |
| `Sublocation` | 子地点 | `features/metadata/domain/iptc_core.dart` |
| `Supplemental categories` | 补充类别 | `features/metadata/domain/iptc_core.dart` |
| `Supplier ID` | 供稿方 ID | `features/metadata/domain/iptc_core.dart` |
| `Supplier image ID` | 供稿图像 ID | `features/metadata/domain/iptc_core.dart` |
| `Title / Slug` | 标题 / Slug | `features/metadata/domain/iptc_core.dart` |
| `Urgency` | 紧急程度 | `features/metadata/domain/iptc_core.dart` |
| `Usage terms` | 使用条款 | `features/metadata/domain/iptc_core.dart` |
| `World region` | 世界地区 | `features/metadata/domain/iptc_core.dart` |
| `Status` | 状态 | `features/metadata/domain/iptc_core.dart、features/metadata/presentation/iptc_editor_dialog.dart、features/metadata/presentation/iptc_template_dialog.dart` |
| `Add to existing` | 添加到现有内容 | `features/metadata/domain/iptc_template.dart` |
| `Append` | 追加 | `features/metadata/domain/iptc_template.dart` |
| `Prefix` | 前缀 | `features/metadata/domain/iptc_template.dart` |
| `Replace` | 替换 | `features/metadata/domain/iptc_template.dart` |
| `Default` | 默认 | `features/metadata/domain/template_snapshots.dart` |
| `Camera model (blank if unknown)` | 相机机型（未知时为空） | `features/metadata/domain/template_variables.dart` |
| `Capture date, YYYY-MM-DD` | 拍摄日期，YYYY-MM-DD | `features/metadata/domain/template_variables.dart` |
| `Capture day, 01–31` | 拍摄日，01–31 | `features/metadata/domain/template_variables.dart` |
| `Capture month, 01–12` | 拍摄月份，01–12 | `features/metadata/domain/template_variables.dart` |
| `Capture time, HH:MM:SS` | 拍摄时间，HH:MM:SS | `features/metadata/domain/template_variables.dart` |
| `Capture year, e.g. 2026 (today's if the photo has no date)` | 拍摄年份，如 2026（照片无日期时用今天） | `features/metadata/domain/template_variables.dart` |
| `File extension without the dot, e.g. ARW` | 不含点的扩展名，如 ARW | `features/metadata/domain/template_variables.dart` |
| `File name with extension, e.g. DSC_0001.ARW` | 含扩展名的文件名，如 DSC_0001.ARW | `features/metadata/domain/template_variables.dart` |
| `File name without extension, e.g. DSC_0001` | 不含扩展名的文件名，如 DSC_0001 | `features/metadata/domain/template_variables.dart` |
| `Lens model (blank if unknown)` | 镜头型号（未知时为空） | `features/metadata/domain/template_variables.dart` |
| `Running number across the applied photos, starting at 1` | 跨应用照片的流水号，从 1 开始 | `features/metadata/domain/template_variables.dart` |
| `Add code` | 添加代码 | `features/metadata/presentation/code_table_dialog.dart` |
| `Code replacements` | 代码替换 | `features/metadata/presentation/code_table_dialog.dart` |
| `Delimiter` | 分隔符 | `features/metadata/presentation/code_table_dialog.dart` |
| `Type a code between the delimiter (e.g. =ff=) in any template field and it expands to its text. Separate alternates with “ \| ” — =ff#2= picks the second.` | 在任意模板字段的分隔符之间输入代码（如 =ff=）即展开为其文本。用“ \| ”分隔候选——=ff#2= 选择第二个。 | `features/metadata/presentation/code_table_dialog.dart` |
| `Type text with a =code= to preview…` | 输入含 =code= 的文本以预览… | `features/metadata/presentation/code_table_dialog.dart` |
| `replacement  (alt1 \| alt2)` | 替换内容（候选1 \| 候选2） | `features/metadata/presentation/code_table_dialog.dart` |
| `Preview` | 预览 | `features/metadata/presentation/code_table_dialog.dart、features/naming/presentation/rename_dialog.dart` |
| `A hot code fills several metadata fields at once: type its =code= in any Metadata-editor field and every field below is stamped (the field you typed in keeps its other text). Values may use =text codes= and {variables}. Uses the same delimiter as the code replacements.` | 一个快捷代码可同时填充多个元数据字段：在任意元数据编辑字段中输入其 =code=，下方每个字段都会被盖印（你输入的字段保留其余文本）。值可以使用 =文本代码= 和 {变量}。与代码替换使用相同的分隔符。 | `features/metadata/presentation/hot_codes_dialog.dart` |
| `Add field` | 添加字段 | `features/metadata/presentation/hot_codes_dialog.dart` |
| `Add hot code` | 添加快捷代码 | `features/metadata/presentation/hot_codes_dialog.dart` |
| `Hot codes` | 快捷代码 | `features/metadata/presentation/hot_codes_dialog.dart` |
| `Remove field` | 移除字段 | `features/metadata/presentation/hot_codes_dialog.dart` |
| `Remove hot code` | 删除快捷代码 | `features/metadata/presentation/hot_codes_dialog.dart` |
| `e.g. arena` | 例如 arena | `features/metadata/presentation/hot_codes_dialog.dart` |
| `${index + 1} of $total` | 第 ${index + 1} / $total 张 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `${topic.label}  ‹ ${topic.parent}` | ${topic.label} ‹ ${topic.parent} | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Artwork or object` | 艺术品或对象 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `City` | 城市 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Clear (use capture time)` | 清除（使用拍摄时间） | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Copy all IPTC fields (⌘/Ctrl+Shift+C)` | 复制全部 IPTC 字段（⌘/Ctrl+Shift+C） | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Copyright` | 版权 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Copyright owners` | 版权所有者 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Could not load the template` | 无法加载模板 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Country` | 国家 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Creator` | 创作者 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Date created` | 创建日期 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Editing $count photos — only fields you change are applied.` | 正在编辑 $count 张照片——仅应用你修改的字段。 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Empty every field and table` | 清空所有字段和表格 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Fill city/state/country from the photo’s GPS position` | 根据照片的 GPS 位置填充城市/省州/国家 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `From GPS` | 来自 GPS | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `From XMP file…` | 来自 XMP 文件… | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `From capture time` | 来自拍摄时间 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Identifier` | 标识符 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Image creators` | 图像创作者 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Item ID` | 条目 ID | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Location` | 地点 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Location ID` | 地点 ID | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Locations shown` | 所示地点 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Media topics` | 媒体主题 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Mixed — leave to keep each photo’s value` | 混合——保留各照片原值 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Name` | 名称 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Next photo — saves edits (⌘/Ctrl+PgDn or ⌘/Ctrl+Enter)` | 下一张——保存修改（⌘/Ctrl+PgDn 或 ⌘/Ctrl+Enter） | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Not set` | 未设置 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Org ID` | 机构 ID | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Paste copied IPTC fields (⌘/Ctrl+Shift+V)` | 粘贴复制的 IPTC 字段（⌘/Ctrl+Shift+V） | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Previous photo — saves edits (⌘/Ctrl+PgUp or ⌘/Ctrl+Shift+Enter)` | 上一张——保存修改（⌘/Ctrl+PgUp 或 ⌘/Ctrl+Shift+Enter） | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Registry entries` | 注册条目 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Save as template` | 另存为模板 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Save as…` | 另存为… | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Save these fields as a named metadata template` | 将这些字段保存为命名元数据模板 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Source` | 来源 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Stamp a metadata template onto the fields` | 将元数据模板盖印到各字段 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Sublocation` | 子地点 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `This photo has no GPS position` | 此照片没有 GPS 位置 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Type to search the IPTC vocabulary…` | 输入以搜索 IPTC 词汇… | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `World region` | 世界地区 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `XMP templates` | XMP 模板 | `features/metadata/presentation/iptc_editor_dialog.dart` |
| `Content` | 内容 | `features/metadata/presentation/iptc_editor_dialog.dart、features/metadata/presentation/iptc_template_dialog.dart` |
| `Rights` | 权利 | `features/metadata/presentation/iptc_editor_dialog.dart、features/metadata/presentation/iptc_template_dialog.dart` |
| `Tables` | 表格 | `features/metadata/presentation/iptc_editor_dialog.dart、features/metadata/presentation/iptc_template_dialog.dart` |
| `Add row` | 添加行 | `features/metadata/presentation/iptc_table_field.dart` |
| `Remove row` | 删除行 | `features/metadata/presentation/iptc_table_field.dart` |
| `Artwork or object` | 艺术品或对象 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Copyright` | 版权 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Copyright owners` | 版权所有者 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Could not load the template` | 无法加载模板 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Could not save the template` | 无法保存模板 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Country` | 国家 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Creator` | 创作者 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Empty every field, keyword and table` | 清空所有字段、关键字和表格 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Identifier` | 标识符 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Image creators` | 图像创作者 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Item ID` | 条目 ID | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Keywords` | 关键字 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Load XMP…` | 加载 XMP… | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Load an XMP template file (Photo Mechanic / Bridge)` | 加载 XMP 模板文件（Photo Mechanic / Bridge） | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Location` | 地点 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Location ID` | 地点 ID | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Locations shown` | 所示地点 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Metadata template` | 元数据模板 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Org ID` | 机构 ID | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Recent values` | 最近使用的值 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Registry entries` | 注册条目 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Save XMP…` | 保存 XMP… | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Save these values as an XMP template file` | 将这些值保存为 XMP 模板文件 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Tick the fields to stamp onto photos. Unticked fields are left untouched. Use {year} {date} {name} {camera} variables and =code= replacements — they expand per photo when applied.` | 勾选要盖印到照片上的字段。未勾选的字段保持原样。可使用 {year} {date} {name} {camera} 变量和 =code= 替换——应用时会按每张照片展开。 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `World region` | 世界地区 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `XMP templates` | XMP 模板 | `features/metadata/presentation/iptc_template_dialog.dart` |
| `Keywords` | 关键字 | `features/metadata/presentation/iptc_template_dialog.dart、features/metadata/presentation/keyword_dialog.dart` |
| `Applies to ${widget.count} photos (replaces their keywords)` | 应用到 ${widget.count} 张照片（替换其关键字） | `features/metadata/presentation/keyword_dialog.dart` |
| `Comma-separated` | 逗号分隔 | `features/metadata/presentation/keyword_dialog.dart` |
| `sunset, beach, portrait` | 日落, 海滩, 人像 | `features/metadata/presentation/keyword_dialog.dart` |
| `Camera` | 相机 | `features/naming/domain/name_element.dart` |
| `Counter` | 计数器 | `features/naming/domain/name_element.dart` |
| `Counter $w` | 计数器（$w 位） | `features/naming/domain/name_element.dart` |
| `Date & time` | 日期与时间 | `features/naming/domain/name_element.dart` |
| `Date (02.07.2026)` | 日期（02.07.2026） | `features/naming/domain/name_element.dart` |
| `Date (02.07.26)` | 日期（02.07.26） | `features/naming/domain/name_element.dart` |
| `Date (2026-07-02)` | 日期（2026-07-02） | `features/naming/domain/name_element.dart` |
| `Date (20260702)` | 日期（20260702） | `features/naming/domain/name_element.dart` |
| `Date / time` | 日期 / 时间 | `features/naming/domain/name_element.dart` |
| `Job name` | 任务名称 | `features/naming/domain/name_element.dart` |
| `Month (Jul)` | 月份（Jul） | `features/naming/domain/name_element.dart` |
| `Month (July)` | 月份（July） | `features/naming/domain/name_element.dart` |
| `Month number (07)` | 月份数字（07） | `features/naming/domain/name_element.dart` |
| `Original filename` | 原始文件名 | `features/naming/domain/name_element.dart` |
| `Time (14-30)` | 时间（14-30） | `features/naming/domain/name_element.dart` |
| `Time (143005)` | 时间（143005） | `features/naming/domain/name_element.dart` |
| `Weekday (Mon)` | 星期（Mon） | `features/naming/domain/name_element.dart` |
| `Weekday (Monday)` | 星期（Monday） | `features/naming/domain/name_element.dart` |
| `Year (2026)` | 年份（2026） | `features/naming/domain/name_element.dart` |
| `Year-month (2026-07)` | 年月（2026-07） | `features/naming/domain/name_element.dart` |
| `Keep filenames` | 保留文件名 | `features/naming/domain/name_preset.dart` |
| `Timestamped` | 时间戳 | `features/naming/domain/name_preset.dart` |
| `Year / date_shoot / name` | 年份 / 日期_拍摄 / 名称 | `features/naming/domain/name_preset.dart` |
| `Year / month / name` | 年份 / 月 / 名称 | `features/naming/domain/name_preset.dart` |
| `$w digit${w == 1 ? '' : 's'}` | $w 位 | `features/naming/presentation/name_builder.dart` |
| `Custom` | 自定义 | `features/naming/presentation/name_builder.dart` |
| `Customise filename` | 自定义文件名 | `features/naming/presentation/name_builder.dart` |
| `Customise filename & folders` | 自定义文件名与文件夹 | `features/naming/presentation/name_builder.dart` |
| `Delete '${selected.name}'` | 删除“${selected.name}” | `features/naming/presentation/name_builder.dart` |
| `Elements` | 元素 | `features/naming/presentation/name_builder.dart` |
| `Example` | 示例 | `features/naming/presentation/name_builder.dart` |
| `Folder` | 文件夹 | `features/naming/presentation/name_builder.dart` |
| `Job name` | 任务名称 | `features/naming/presentation/name_builder.dart` |
| `Optional sub-folders, e.g. {YYYY}/{MM}` | 可选子文件夹，如 {YYYY}/{MM} | `features/naming/presentation/name_builder.dart` |
| `Preset actions` | 预设操作 | `features/naming/presentation/name_builder.dart` |
| `Preset name` | 预设名称 | `features/naming/presentation/name_builder.dart` |
| `Save as new preset…` | 另存为新预设… | `features/naming/presentation/name_builder.dart` |
| `Save naming preset` | 保存命名预设 | `features/naming/presentation/name_builder.dart` |
| `Type here, or insert elements below…` | 在此输入，或在下方插入元素… | `features/naming/presentation/name_builder.dart` |
| `e.g. Wedding-Anna (used by the Job-name element)` | 如 Wedding-Anna（供 Job-name 元素使用） | `features/naming/presentation/name_builder.dart` |
| `Job name (the Job-name element)` | 任务名称（Job-name 元素） | `features/naming/presentation/rename_dialog.dart` |
| `Rename $count photo${count == 1 ? '' : 's'}` | 重命名 $count 张照片 | `features/naming/presentation/rename_dialog.dart` |
| `Rename ${widget.sources.length}` | 重命名 ${widget.sources.length} 张 | `features/naming/presentation/rename_dialog.dart` |
| `Renames the files in place (with their .xmp sidecars). Name clashes get a _2, _3… suffix.` | 就地重命名文件（连同 .xmp 附属文件）。名称冲突会自动加 _2、_3… 后缀。 | `features/naming/presentation/rename_dialog.dart` |
| `…and ${widget.sources.length - 4} more` | …以及另外 ${widget.sources.length - 4} 张 | `features/naming/presentation/rename_dialog.dart` |
| `A fast, cross-platform photo culling app. Ingest, cull, filter, export, hand off — speed is the product.` | 一款快速的跨平台照片筛选应用。导入、筛选、过滤、导出、移交——速度即产品。 | `features/settings/presentation/diagnostics.dart` |
| `Cullimingo Logs` | Cullimingo 日志 | `features/settings/presentation/diagnostics.dart` |
| `Recommended` | 推荐 | `features/settings/presentation/performance_preset_selector.dart` |
| `About & licenses` | 关于与许可 | `features/settings/presentation/settings_dialog.dart` |
| `Access token (cs_pat_…)` | 访问令牌（cs_pat_…） | `features/settings/presentation/settings_dialog.dart` |
| `Add editor…` | 添加编辑器… | `features/settings/presentation/settings_dialog.dart` |
| `Add server…` | 添加服务器… | `features/settings/presentation/settings_dialog.dart` |
| `Applies the next time you start Cullimingo.` | 在下次启动 Cullimingo 时生效。 | `features/settings/presentation/settings_dialog.dart` |
| `Apply ratings, flags and colours to the whole bracket` | 将评分、标记和色标应用到整个包围曝光 | `features/settings/presentation/settings_dialog.dart` |
| `Apply to photos as they are ingested` | 照片导入时应用 | `features/settings/presentation/settings_dialog.dart` |
| `Auto-advance to the next photo after rating or flagging` | 评分或标记后自动跳到下一张 | `features/settings/presentation/settings_dialog.dart` |
| `Caption, credit, location… to stamp onto photos, saved as named templates you can switch per customer or assignment. Use {year}/{name}/{camera}… variables and =code= replacements; the active template applies with the ⋮ menu, T, or automatically on ingest.` | 要盖印到照片上的说明、署名、地点…，保存为可按客户或任务切换的命名模板。可使用 {year}/{name}/{camera}… 变量和 =code= 替换；活动模板通过 ⋮ 菜单、T 键或导入时自动应用。 | `features/settings/presentation/settings_dialog.dart` |
| `Check for updates on startup` | 启动时检查更新 | `features/settings/presentation/settings_dialog.dart` |
| `Clear thumbnail cache` | 清除缩略图缓存 | `features/settings/presentation/settings_dialog.dart` |
| `Code replacements (${_codes.codes.length})…` | 代码替换（${_codes.codes.length}）… | `features/settings/presentation/settings_dialog.dart` |
| `Code replacements…` | 代码替换… | `features/settings/presentation/settings_dialog.dart` |
| `Cullimingo · Version $kAppVersion` | Cullimingo · 版本 $kAppVersion | `features/settings/presentation/settings_dialog.dart` |
| `Delete template` | 删除模板 | `features/settings/presentation/settings_dialog.dart` |
| `Delivery` | 交付 | `features/settings/presentation/settings_dialog.dart` |
| `Delivery servers` | 交付服务器 | `features/settings/presentation/settings_dialog.dart` |
| `Edit "$name" (${_templateFieldCount()} fields)…` | 编辑“$name”（${_templateFieldCount()} 个字段）… | `features/settings/presentation/settings_dialog.dart` |
| `Edit server` | 编辑服务器 | `features/settings/presentation/settings_dialog.dart` |
| `Expand pulled-in client picks (Find / ContactSheet) to their brackets automatically` | 把拉取的客户精选（查找 / ContactSheet）自动扩展到其包围曝光 | `features/settings/presentation/settings_dialog.dart` |
| `Exposure brackets` | 包围曝光 | `features/settings/presentation/settings_dialog.dart` |
| `FTP/FTPS/SFTP destinations the export dialog can upload to (wire/agency delivery). Passwords are stored in the system keychain, not in the settings file.` | 导出对话框可上传到的 FTP/FTPS/SFTP 目标（通讯社/机构交付）。密码保存在系统钥匙串中，而非设置文件。 | `features/settings/presentation/settings_dialog.dart` |
| `Flash a confirmation over the loupe when you mark a photo` | 标记照片时在放大视图上闪烁确认 | `features/settings/presentation/settings_dialog.dart` |
| `General` | 常规 | `features/settings/presentation/settings_dialog.dart` |
| `Hand the selected photos to another app from the right-click menu; the first editor is ⌘E.` | 从右键菜单把所选照片交给其他应用；第一个编辑器为 ⌘E。 | `features/settings/presentation/settings_dialog.dart` |
| `Hot codes (${_hotCodes.codes.length})…` | 快捷代码（${_hotCodes.codes.length}）… | `features/settings/presentation/settings_dialog.dart` |
| `Hot codes…` | 快捷代码… | `features/settings/presentation/settings_dialog.dart` |
| `Ingest` | 导入 | `features/settings/presentation/settings_dialog.dart` |
| `Interface` | 界面 | `features/settings/presentation/settings_dialog.dart` |
| `Metadata templates` | 元数据模板 | `features/settings/presentation/settings_dialog.dart` |
| `New template` | 新建模板 | `features/settings/presentation/settings_dialog.dart` |
| `No saved templates` | 没有已保存模板 | `features/settings/presentation/settings_dialog.dart` |
| `Open Import automatically when a memory card is inserted` | 插入存储卡时自动打开导入 | `features/settings/presentation/settings_dialog.dart` |
| `Performance` | 性能 | `features/settings/presentation/settings_dialog.dart` |
| `Remove server` | 删除服务器 | `features/settings/presentation/settings_dialog.dart` |
| `Rename template` | 重命名模板 | `features/settings/presentation/settings_dialog.dart` |
| `Reopen last folders on startup` | 启动时重新打开上次文件夹 | `features/settings/presentation/settings_dialog.dart` |
| `Send to editors` | 发送到编辑器 | `features/settings/presentation/settings_dialog.dart` |
| `Set up template…` | 设置模板… | `features/settings/presentation/settings_dialog.dart` |
| `Show button tooltips` | 显示按钮提示 | `features/settings/presentation/settings_dialog.dart` |
| `Startup` | 启动 | `features/settings/presentation/settings_dialog.dart` |
| `Thumbnail cache cleared` | 缩略图缓存已清除 | `features/settings/presentation/settings_dialog.dart` |
| `View logs` | 查看日志 | `features/settings/presentation/settings_dialog.dart` |
| `Blue` | 蓝 | `shared/models/cull_marks.dart` |
| `Green` | 绿 | `shared/models/cull_marks.dart` |
| `None` | 无 | `shared/models/cull_marks.dart` |
| `Purple` | 紫 | `shared/models/cull_marks.dart` |
| `Red` | 红 | `shared/models/cull_marks.dart` |
| `Yellow` | 黄 | `shared/models/cull_marks.dart` |
| `Choose…` | 选择… | `shared/widgets/dialog_kit.dart` |
| `Customer / assignment name` | 客户 / 任务名称 | `shared/widgets/dialog_kit.dart` |
