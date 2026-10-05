# -*- coding: utf-8 -*-
"""en→zh rules for Cullimingo UI strings. PER_FILE wins over GLOBAL."""

# (old, new) applied in any file except when PER_FILE has the same old for that file
GLOBAL = {
    'Cancel': '取消',
    'Import': '导入',
    'Export': '导出',
    'Delete': '删除',
    'Settings': '设置',
    'Open folder': '打开文件夹',
    'Open folder…': '打开文件夹…',
    'Metadata': '元数据',
    'Grouping': '分组',
    'Remove': '移除',
    'Change': '更换',
    'Reload': '重新加载',
    'Loading…': '正在加载…',
    'Browse…': '浏览…',
    'Choose…': '选择…',
    'Preview': '预览',
    'Example': '示例',
    'Keywords': '关键字',
    'Password': '密码',
    'Server': '服务器',
    'Gallery': '画廊',
    'Destination': '目标位置',
    'Camera': '相机',
    'Filename': '文件名',
    'Custom': '自定义',
    'Append': '追加',
    'Replace': '替换',
    'Prefix': '前缀',
    'Normal': '正常',
    'Ascending': '升序',
    'Descending': '降序',
    'Recommended': '推荐',
    'Original': '原始',
    'Format': '格式',
    'Quality': '质量',
    'Naming': '命名',
    'Output': '输出',
    'Subfolder': '子文件夹',
    'Height': '高度',
    'Content': '内容',
    'Rights': '权利',
    'Tables': '表格',
    'Folder': '文件夹',
    'Orientation': '方向',
    'Resolution': '分辨率',
    'Dimensions': '尺寸',
    'Exposure': '曝光',
    'Aperture': '光圈',
    'Focal length': '焦距',
    'Captured': '拍摄时间',
    'Source': '来源',
    'Status': '状态',
    'Reject': '剔除',
    'Select': '选择',
}

P = {}  # file -> {old: new}

def add(file, old, new):
    P.setdefault(file, {})[old] = new

F = 'lib/features/'
S = 'lib/shared/'

# ---------- filter domain/presentation ----------
add(F+'filter/domain/photo_sort.dart', 'Capture Time', '拍摄时间')
add(F+'filter/domain/photo_sort.dart', 'Modification Time', '修改时间')
add(F+'filter/domain/photo_sort.dart', 'Rating', '星级')
add(F+'filter/domain/photo_sort.dart', 'Color Class', '色标类别')
add(F+'filter/domain/photo_sort.dart', 'Lens', '镜头')
add(F+'filter/domain/photo_sort.dart', 'Width', '宽度')

fb = F+'filter/presentation/filter_bar.dart'
add(fb, 'All (${all.length})', '全部（${all.length}）')
add(fb, 'Selected ($selectedCount)', '已选（$selectedCount）')
add(fb, 'Picks (${count((p) => p.flag == PickFlag.pick)})', '精选（${count((p) => p.flag == PickFlag.pick)}）')
add(fb, 'Rejected (${count((p) => p.flag == PickFlag.reject)})', '已剔除（${count((p) => p.flag == PickFlag.reject)}）')
add(fb, 'Keyworded (${count((p) => p.keywords.isNotEmpty)})', '已加关键字（${count((p) => p.keywords.isNotEmpty)}）')
add(fb, 'Bursts', '连拍')
add(fb, 'Similar', '相似')
add(fb, 'Stack brackets ($bracketCount)', '堆叠包围曝光（$bracketCount）')
add(fb, 'Hide JPEG ($pairCount)', '隐藏 JPEG（$pairCount）')
add(fb, 'JPEG only ($jpegCount)', '仅 JPEG（$jpegCount）')
add(fb, 'RAW only ($rawCount)', '仅 RAW（$rawCount）')
add(fb, 'All file types', '全部文件类型')
add(fb, 'Search filename…', '搜索文件名…')
add(fb, 'Filter presets', '筛选预设')
add(fb, 'Save current filter…', '保存当前筛选…')
add(fb, 'Save filter preset', '保存筛选预设')
add(fb, 'Preset name', '预设名称')
add(fb, 'Rating ≥ $star', '星级 ≥ $star')
add(fb, 'Filter: ${label.displayName} label', '筛选：${label.displayName} 色标')
add(fb, '${label.displayName} label — showing only these', '只看 ${label.displayName} 色标')
add(fb, '$groupLabel ($groupCount)', '$groupLabel（$groupCount）')

# ---------- cull domain ----------
cs = F+'cull/domain/cull_shortcuts.dart'
add(cs, 'Pick', '精选')
add(cs, 'Loupe', '放大视图')
add(cs, 'Clear rating', '清除星级')
for i in range(1, 6):
    add(cs, f'Rate {i}', f'评 {i} 星')
add(cs, 'Colour: red', '色标：红')
add(cs, 'Colour: yellow', '色标：黄')
add(cs, 'Colour: green', '色标：绿')
add(cs, 'Colour: blue', '色标：蓝')
add(cs, 'Colour: purple', '色标：紫')
add(cs, 'Compare selected', '对比已选')
add(cs, "Compare focused photo's group", '对比焦点照片的组')
add(cs, 'Info inspector', '信息检查器')
add(cs, 'Edit keywords', '编辑关键字')
add(cs, 'Edit metadata', '编辑元数据')
add(cs, 'Apply metadata template', '应用元数据模板')
add(cs, 'Rename…', '重命名…')
add(cs, 'Rotate right', '向右旋转')
add(cs, 'Rotate left', '向左旋转')
add(cs, 'Expand selection to bracket', '扩展选择到包围曝光')
add(cs, 'Space', '空格')
add(cs, 'Backspace', '退格')
add(cs, 'Enter', '回车')
add(cs, 'Tab', 'Tab')

mu = F+'cull/domain/mark_undo.dart'
add(mu, '$noun ($photoCount photos)', '$noun（$photoCount 张）')
add(mu, 'rating', '星级')
add(mu, 'flag', '标记')
add(mu, 'colour label', '色标')
add(mu, 'rotation', '旋转')
add(mu, 'stack', '堆叠')
add(mu, 'unstack', '取消堆叠')

ss = F+'cull/domain/similarity_sensitivity.dart'
add(ss, 'Strict', '严格')
add(ss, 'Near-duplicates only', '仅近似重复')
add(ss, 'Balanced', '均衡')
add(ss, 'Same subject / burst', '同主体 / 连拍')
add(ss, 'Loose', '宽松')
add(ss, 'Similar scenes', '相似场景')

# ---------- cull widgets / presentation ----------
tb = F+'cull/presentation/widgets/cull_top_bar.dart'
add(tb, 'Library', '图库')
add(tb, '$count photos', '$count 张')
add(tb, 'Open folder (⌘/Ctrl O)', '打开文件夹（⌘/Ctrl O）')
add(tb, 'Open folder: including sub-folders', '打开文件夹：包含子文件夹')
add(tb, 'Open folder: top level only', '打开文件夹：仅顶层')
add(tb, 'Find by filename (⌘F)', '按文件名查找（⌘F）')
add(tb, 'Show info (I)', '显示信息（I）')
add(tb, 'Hide info (I)', '隐藏信息（I）')
add(tb, 'Keyboard shortcuts (?)', '键盘快捷键（?）')
add(tb, 'Sort by', '排序方式')
add(tb, 'Compare selected (C)', '对比已选（C）')
add(tb, 'Expand selection to bracket (G)', '扩展选择到包围曝光（G）')
add(tb, 'Edit keywords (K)', '编辑关键字（K）')
add(tb, 'Apply metadata template (T)', '应用元数据模板（T）')
add(tb, 'Find similar photos', '查找相似照片')
add(tb, 'Clear similar grouping', '清除相似分组')
add(tb, 'Apply marks to whole bracket', '将标记应用到整个包围曝光')
add(tb, 'Fill location from GPS', '从 GPS 填充位置')
add(tb, 'Import selection list…', '导入选择列表…')
add(tb, 'Refresh folder (⌘R)', '刷新文件夹（⌘R）')
add(tb, 'Re-sync sidecars from disk', '从磁盘重新同步附属文件')
add(tb, 'Delete rejected photos… (⌘⌫)', '删除已剔除照片…（⌘⌫）')
add(tb, 'Saved selections', '已保存选择')
add(tb, '${selection.name} (${selection.photoIds.length})', '${selection.name}（${selection.photoIds.length}）')
add(tb, 'Save current selection…', '保存当前选择…')
add(tb, 'Syncing $pending…', '正在同步 $pending…')
add(tb, 'Writing marks to XMP sidecars', '正在将标记写入 XMP 附属文件')

ct = F+'cull/presentation/widgets/cull_toolbar.dart'
add(ct, 'Pick (P)', '精选（P）')
add(ct, 'Reject (X)', '剔除（X）')
add(ct, 'Rate $i', '评 $i 星')
add(ct, 'Keywords (K)', '关键字（K）')
add(ct, "Keywords: ${photo.keywords.join(', ')}", '关键字：${photo.keywords.join(\', \')}')
add(ct, 'Edit metadata (M)', '编辑元数据（M）')
add(ct, '${label.name} ($key)', '${label.name}（$key）')

add(F+'cull/presentation/widgets/cull_tab_bar.dart', 'Open another folder', '打开另一个文件夹')
add(F+'cull/presentation/widgets/cull_tab_bar.dart', 'Open folder / recent', '打开文件夹 / 最近')

es = F+'cull/presentation/widgets/empty_states.dart'
add(es, 'Open a folder of RAWs or JPEGs to start culling', '打开 RAW 或 JPEG 文件夹开始筛选')
add(es, 'Open folder', '打开文件夹')
add(es, 'Version $kAppVersion', '版本 $kAppVersion')
add(es, 'No photos match the current filter', '没有符合当前筛选的照片')
add(es, 'Clear filters', '清除筛选')

sb = F+'cull/presentation/widgets/status_bar.dart'
add(sb, "$total photo${total == 1 ? '' : 's'}", '$total 张照片')
add(sb, '$filteredCount of $total photos', '$total 张中的 $filteredCount 张')
add(sb, ' · $selectedCount selected', ' · 已选 $selectedCount 张')
add(sb, 'Export $n selected', '导出已选 $n 张')
add(sb, "Export $n photo${n == 1 ? '' : 's'}", '导出 $n 张照片')
add(sb, 'Export (⌘/Ctrl S)', '导出（⌘/Ctrl S）')

add(F+'cull/presentation/widgets/export_bar.dart', 'Exporting', '导出')
add(F+'cull/presentation/widgets/export_bar.dart', '$verb $done of $total…', '$verb $done / $total…')
add(F+'cull/presentation/widgets/notice_bar.dart', 'Dismiss', '关闭')

pc = F+'cull/presentation/widgets/photo_cell.dart'
add(pc, 'Sidecar changed outside Cullimingo (resolved newest-wins)', '附属文件在 Cullimingo 外被修改（按最新内容解决）')
add(pc, 'Cropped in Lightroom / Camera Raw', '在 Lightroom / Camera Raw 中裁剪过')

lv = F+'cull/presentation/widgets/loupe_view.dart'
add(lv, 'Close loupe (Esc)', '关闭放大视图（Esc）')
add(lv, 'Can’t display this file', '无法显示此文件')
add(lv, 'Open in system player', '在系统播放器中打开')
add(lv, 'Show crop outline', '显示裁剪框')
add(lv, 'Hide crop outline', '隐藏裁剪框')
add(lv, 'Show filmstrip', '显示胶片条')
add(lv, 'Hide filmstrip', '隐藏胶片条')
add(lv, 'Histogram', '直方图')
add(lv, 'Clipping warnings', '过曝警告')
add(lv, 'Focus peaking', '峰值对焦')
add(lv, 'Analysis overlays', '分析叠加层')
add(lv, 'No rating', '无星级')
add(lv, 'Pick', '已精选')
add(lv, 'Rejected', '已剔除')
add(lv, 'Flag cleared', '已清除标记')
add(lv, 'Colour cleared', '已清除色标')

cv = F+'cull/presentation/widgets/compare_view.dart'
add(cv, 'Compare $count photos', '对比 $count 张照片')
add(cv, 'Arrows focus · 1-5 / P / X / colours mark · ✕ drops · Esc closes',
       '方向键聚焦 · 1-5 / P / X / 色标标记 · ✕ 移除 · Esc 关闭')
add(cv, 'Close compare (Esc)', '关闭对比（Esc）')
add(cv, 'Remove from compare', '从对比中移除')

tm = F+'cull/presentation/widgets/thumbnail_context_menu.dart'
add(tm, 'Edit metadata…', '编辑元数据…')
add(tm, 'Edit keywords…', '编辑关键字…')
add(tm, 'Apply marks to bracket', '应用标记到包围曝光')
add(tm, 'Stack as bracket', '堆叠为包围曝光')
add(tm, 'Remove from bracket', '从包围曝光中移除')
add(tm, 'Copy to folder…', '复制到文件夹…')
add(tm, 'Move to folder…', '移动到文件夹…')
add(tm, 'Send to ContactSheet…', '发送到 ContactSheet…')
add(tm, 'Pull marks from ContactSheet…', '从 ContactSheet 拉取标记…')
add(tm, 'Open in default app', '在默认应用中打开')
add(tm, 'Open in ${editor.label}', '在 ${editor.label} 中打开')
add(tm, 'Export…', '导出…')
add(tm, 'Delete…', '删除…')
add(tm, 'Expand selection to bracket', '扩展选择到包围曝光')
add(tm, 'Rotate left', '向左旋转')
add(tm, 'Rotate right', '向右旋转')

kd = F+'cull/presentation/widgets/keyboard_shortcuts_dialog.dart'
add(kd, 'View & select', '查看与选择')
add(kd, 'Rate, flag & label', '评分、标记与色标')
add(kd, 'Navigation & app', '导航与应用')
add(kd, 'Move focus', '移动焦点')
add(kd, 'Open loupe / play video', '打开放大视图 / 播放视频')
add(kd, 'Loupe (also opens it)', '放大视图（同样打开）')
add(kd, 'Previous / next photo in loupe', '放大视图中上一张 / 下一张')
add(kd, 'Close loupe / compare', '关闭放大视图 / 对比')
add(kd, 'New tab', '新标签页')
add(kd, 'Close tab', '关闭标签页')
add(kd, 'Refresh folder', '刷新文件夹')
add(kd, 'Find by filename', '按文件名查找')
add(kd, 'Select all (filtered)', '全选（筛选结果）')
add(kd, 'Show this list', '显示此列表')
add(kd, 'Delete rejected photos…', '删除已剔除照片…')
add(kd, 'Undo mark change', '撤销标记更改')
add(kd, 'Redo mark change', '重做标记更改')
add(kd, 'Metadata editor: save & next photo', '元数据编辑器：保存并跳下一张')
add(kd, 'Metadata editor: previous photo', '元数据编辑器：上一张')
add(kd, 'Add to selection', '加入选择')
add(kd, 'Rate 1–5 stars', '评 1–5 星')
add(kd, 'Pick / reject', '精选 / 剔除')
add(kd, 'Colour labels', '色标')
add(kd, 'Open the loupe', '打开放大视图')
add(kd, 'Culling here is keyboard-first. The essentials to get going:', '本应用以键盘操作为主。入门要点：')
add(kd, 'Got it', '知道了')
add(kd, 'Customize…', '自定义…')
add(kd, 'Welcome to Cullimingo', '欢迎使用 Cullimingo')

ke = F+'cull/presentation/widgets/keyboard_shortcuts_editor.dart'
add(ke, 'Customize shortcuts', '自定义快捷键')
add(ke, 'Reset to defaults', '恢复默认')
add(ke, 'Press a key…', '按任意键…')

dr = F+'cull/presentation/widgets/delete_rejects_dialog.dart'
add(dr, 'Delete rejected photos', '删除已剔除照片')
add(dr, 'Delete photo', '删除照片')
add(dr, 'Delete $count photos', '删除 $count 张照片')
add(dr, 'rejected photo', '已剔除照片')
add(dr, 'rejected photos', '已剔除照片')
add(dr, 'Move to Trash', '移到废纸篓')

add(F+'cull/presentation/widgets/find_similar_dialog.dart', 'Sensitivity', '敏感度')
add(F+'cull/presentation/widgets/find_similar_dialog.dart', 'Find similar', '查找相似')

# ---------- cull page parts ----------
add(F+'cull/presentation/cull_page.dart', 'Error: $e', '错误：$e')

ck = F+'cull/presentation/cull_page.keyboard.dart'
add(ck, 'Nothing to undo', '没有可撤销的操作')
add(ck, 'Undid $undone', '已撤销 $undone')
add(ck, 'Nothing to redo', '没有可重做的操作')
add(ck, 'Redid $redone', '已重做 $redone')

sl = F+'cull/presentation/cull_page.selections.dart'
add(sl, ' (+$extra bracket frames)', '（另含 $extra 张包围曝光）')
add(sl, 'Expanded ${selected.length} → ${expanded.length} photos', '已从 ${selected.length} 张扩展到 ${expanded.length} 张')
add(sl, 'No bracket members to add', '没有可添加的包围曝光成员')
add(sl, 'Applied marks to $n bracket frame(s)', '已将标记应用到 $n 张包围曝光')
add(sl, 'Stacked $n photos', '已堆叠 $n 张照片')
add(sl, 'Unstacked $n photos', '已取消堆叠 $n 张照片')
add(sl, 'Only RAWs (skip JPEG twins)', '仅 RAW（跳过对应 JPEG）')
add(sl, 'Find photos by filename', '按文件名查找照片')
add(sl, 'Import selection list', '导入选择列表')
add(sl, '$nameCount name(s) from $fileName.', '来自 $fileName 的 $nameCount 个名称。')
add(sl, 'Select photos first to save a selection', '请先选择照片再保存选择')
add(sl, 'Save selection', '保存选择')
add(sl, 'Selection name', '选择名称')
add(sl, 'Saved "${name.trim()}" (${ids.length} photo(s))', '已保存“${name.trim()}”（${ids.length} 张）')
add(sl, 'Deleted "${selection.name}"', '已删除“${selection.name}”')
add(sl, 'Loaded "${selection.name}" (${selection.photoIds.length})', '已加载“${selection.name}”（${selection.photoIds.length} 张）')
add(sl, 'Import', '导入')

wsp = F+'cull/presentation/cull_page.workspace.dart'
add(wsp, 'The folder is no longer available (ejected or deleted)', '文件夹已不可用（已弹出或删除）')
add(wsp, "Card '${card.name}' detected", '检测到存储卡“${card.name}”')
add(wsp, 'No metadata template set up — add one in Settings', '尚未设置元数据模板——请在设置中添加')
add(wsp, 'Applied the metadata template to ${outcome.count} photo(s)', '已将元数据模板应用到 ${outcome.count} 张照片')
add(wsp, 'Stamped the metadata template onto $stamped ingested photo(s)', '已将元数据模板盖印到 $stamped 张导入照片')
add(wsp, 'Sidecars already up to date', '附属文件已是最新')
add(wsp, 'Updated ${result.updated} photo(s) from disk$conflicts', '已从磁盘更新 ${result.updated} 张照片$conflicts')
add(wsp, 'Select photos to fill their location from GPS', '请选择照片以从 GPS 填充位置')
add(wsp, '${outcome.noGps} without GPS', '${outcome.noGps} 张无 GPS')
add(wsp, '${outcome.noPlace} with no place nearby', '${outcome.noPlace} 张附近无地点')
add(wsp, 'No location filled — $skipped', '未填充位置——$skipped')
add(wsp, 'Select photos to apply the template to', '请选择要应用模板的照片')
add(wsp, 'Folder up to date', '文件夹已是最新')
add(wsp, '${marks.updated} mark(s) from disk', '来自磁盘的 ${marks.updated} 条标记')
add(wsp, '+${scan.added} / −${scan.removed} file(s)', '+${scan.added} / −${scan.removed} 个文件')
add(wsp, ' · ${marks.conflicts} conflict(s)', ' · ${marks.conflicts} 个冲突')
add(wsp, ' · ${result.conflicts} conflict(s)', ' · ${result.conflicts} 个冲突')
add(wsp, '$missing saved folder(s) no longer available', '$missing 个已保存的文件夹不再可用')
add(wsp, 'Thumbnail cache cleared', '缩略图缓存已清除')
add(wsp, 'Synced ${parts.join(\' · \')}$conflicts$unreadable', '已同步 ${parts.join(\' · \')}$conflicts$unreadable')

cj = F+'cull/presentation/cull_page.jobs.dart'
add(cj, 'No rejected photos in this folder', '此文件夹没有已剔除照片')
add(cj, '${failed.length} failed', '${failed.length} 个失败')
add(cj, '${summary.failed} failed', '${summary.failed} 个失败')
add(cj, '${summary.unchanged} unchanged', '${summary.unchanged} 个未更改')
add(cj, 'Moved ${result.deleted} $noun to the Trash', '已将 ${result.deleted} 个$noun 移到废纸篓')
add(cj, 'Renamed ${summary.renamed} photo(s)', '已重命名 ${summary.renamed} 张照片')
add(cj, 'No editors configured yet — add one in Settings', '尚未配置编辑器——请在设置中添加')
add(cj, 'Cleared similar grouping', '已清除相似分组')
add(cj, 'Performance set to ${changed.label} — restart Cullimingo to apply', '性能已设为 ${changed.label}——重启 Cullimingo 后生效')

add(F+'cull/presentation/cull_page.notices.dart', 'Cullimingo ${update.version} is available.', 'Cullimingo ${update.version} 已可用。')
add(F+'cull/presentation/cull_page.notices.dart', 'Download', '下载')

add(F+'cull/presentation/background_jobs.dart', 'Exporting', '导出')
add(F+'cull/presentation/background_jobs.dart', 'Finding similar', '查找相似')

jr = F+'cull/presentation/cull_job_runner.dart'
add(jr, 'Exported ${summary.written} photo(s) · $failed failed', '已导出 ${summary.written} 张照片 · $failed 个失败')
add(jr, 'Exported ${summary.written} photo(s)', '已导出 ${summary.written} 张照片')
add(jr, 'Export cancelled', '导出已取消')
add(jr, 'Uploading', '上传')
add(jr, 'Delivered ${summary.delivered} photo(s) to ${server.name}', '已交付 ${summary.delivered} 张照片到 ${server.name}')
add(jr, 'Sent $uploaded photo(s) to ContactSheet', '已发送 $uploaded 张照片到 ContactSheet')
add(jr, 'Rendering', '渲染')
add(jr, 'Nothing was rendered to upload', '没有可上传的渲染结果')
add(jr, '$renderFailed failed to render', '$renderFailed 张渲染失败')
add(jr, '${failures.length} failed to upload (${failures.first.error})', '${failures.length} 个上传失败（${failures.first.error}）')
add(jr, 'Send cancelled', '发送已取消')
add(jr, 'Applying', '应用')
add(jr, 'Pulling', '拉取')
add(jr, '${resolved.length} marked photo(s)', '${resolved.length} 张已标记照片')
add(jr, '$savedCollections collection(s)', '$savedCollections 个收藏')
add(jr, 'No matching client marks in “${request.galleryName}”', '“${request.galleryName}” 中没有匹配的客户标记')
add(jr, "Pulled ${parts.join(' + ')} from “${request.galleryName}”", '已从“${request.galleryName}”拉取 ${parts.join(\' + \')}')
add(jr, 'No similar photos found (${sensitivity.label} sensitivity)', '未找到相似照片（${sensitivity.label} 敏感度）')
add(jr, 'Transfer cancelled', '传输已取消')
add(jr, 'Moving', '移动')
add(jr, 'Copying', '复制')
add(jr, "${isMove ? 'Move' : 'Copy'} not started: ${check.problems.join(' ')}", '无法开始${isMove ? \'移动\' : \'复制\'}：${check.problems.join(\' \')}')
add(jr, "${isMove ? 'Moved' : 'Copied'} ${summary.transferred} photo(s)", '已${isMove ? \'移动\' : \'复制\'} ${summary.transferred} 张照片')
add(jr, '${summary.conflicts} skipped (name in use)', '${summary.conflicts} 个跳过（名称被占用）')
add(jr, '${summary.stillBeingWritten} still being written (retry)', '${summary.stillBeingWritten} 个仍在写入（请重试）')
add(jr, 'No gallery to upload into', '没有可上传的画廊')

# ---------- inspector ----------
ip = F+'inspector/presentation/inspector_panel.dart'
add(ip, 'Camera', '相机')
add(ip, 'Aperture', '光圈')
add(ip, 'Exp. comp.', '曝光补偿')
add(ip, 'Focal length', '焦距')
add(ip, 'Resolution', '分辨率')
add(ip, 'Dimensions', '尺寸')
add(ip, 'Orientation', '方向')
add(ip, 'Captured', '拍摄时间')
add(ip, 'No caption or credit', '无说明或署名')
add(ip, 'Locations shown', '所示地点')
add(ip, 'Artwork or object', '艺术品或对象')
add(ip, 'Image creators', '图像创作者')
add(ip, 'Copyright owners', '版权所有者')
add(ip, 'Licensors', '许可方')
add(ip, 'Registry entries', '注册条目')
add(ip, '+ Add field', '添加字段')
add(ip, 'Add a metadata field', '添加元数据字段')
add(ip, 'No marks', '无标记')
add(ip, 'No photo selected', '未选择照片')

ef = F+'inspector/domain/exif_format.dart'
add(ef, 'Mirrored', '镜像')
add(ef, 'Rotated 180°', '旋转 180°')
add(ef, 'Mirrored, 180°', '镜像，180°')
add(ef, 'Mirrored, 90° CCW', '镜像，逆时针 90°')
add(ef, 'Rotated 90° CW', '顺时针旋转 90°')
add(ef, 'Mirrored, 90° CW', '镜像，顺时针 90°')
add(ef, 'Rotated 90° CCW', '逆时针旋转 90°')

# ---------- ingest ----------
ig = F+'ingest/presentation/ingest_dialog.dart'
add(ig, 'Import photos', '导入照片')
add(ig, 'Select a card or folder', '选择存储卡或文件夹')
add(ig, 'Source', '来源')
add(ig, 'Choose where the photos are copied…', '选择照片复制目标…')
add(ig, 'Include JPEGs', '包含 JPEG')
add(ig, 'Uncheck to import RAW files only', '取消勾选则仅导入 RAW 文件')
add(ig, 'Include videos', '包含视频')
add(ig, 'Videos are copied alongside the photos', '视频将随照片一起复制')
add(ig, 'Also copy to a backup destination (always verified)', '同时复制到备份目标（始终校验）')
add(ig, 'Choose backup…', '选择备份位置…')
add(ig, 'Verify each copy by checksum (recommended)', '通过校验和验证每次复制（推荐）')
add(ig, 'Days on this card — $included of ${counts.length} included', '此卡上的日期——已包含 $included / ${counts.length} 天')
add(ig, 'Newest day', '最新一天')
add(ig, 'Today · $date', '今天 · $date')
add(ig, 'Yesterday · $date', '昨天 · $date')
add(ig, '${_dayMonths[d.month - 1]} ${d.day}', '${d.month}月${d.day}日')
add(ig, '${v.name}  •  card', '${v.name} • 存储卡')
add(ig, 'Select a card or folder to scan.', '选择要扫描的存储卡或文件夹。')
add(ig, 'Everything is filtered out — re-include a day or file type.', '全部已被筛选排除——请重新包含某个日期或文件类型。')
add(ig, 'No photos found in the source.', '来源中未找到照片。')
add(ig, "Couldn't scan this source: $_scanError", '无法扫描此来源：$_scanError')
add(ig, 'Scanning…', '正在扫描…')
add(ig, 'Checking destinations…', '正在检查目标…')
add(ig, 'Starting…', '正在开始…')
add(ig, 'Choose a destination to import', '选择导入目标位置')
add(ig, 'Choose the backup destination', '选择备份目标位置')
add(ig, 'Select a source above', '请在上方选择来源')
add(ig, 'Import complete', '导入完成')
add(ig, 'Import finished with issues', '导入完成但有问题')
add(ig, 'Import cancelled', '导入已取消')
add(ig, 'Importing…', '正在导入…')
add(ig, "Import $count photo${count == 1 ? '' : 's'}", '导入 $count 张照片')
add(ig, 'Cancelling…', '正在取消…')
add(ig, 'Open in library', '在图库中打开')
add(ig, 'Copied & verified', '已复制并校验')
add(ig, 'Copied (only the backup verified)', '已复制（仅备份已校验）')
add(ig, 'Copied (not verified)', '已复制（未校验）')
add(ig, 'Already present (skipped)', '已存在（已跳过）')
add(ig, 'Not copied (cancelled)', '未复制（已取消）')
add(ig, 'Conflicts (kept existing)', '冲突（保留现有文件）')
add(ig, 'Still being written (import again)', '仍在写入（请重新导入）')
add(ig, 'Failed', '失败')
add(ig, "Couldn't read on the source", '在来源上无法读取')
add(ig, '• ${p.basename(r.source)}: ${r.message ?? r.outcome.name}', '• ${p.basename(r.source)}：${r.message ?? r.outcome.name}')
add(ig, '• ${shown(u.path)}: ${u.reason}', '• ${shown(u.path)}：${u.reason}')
add(ig, '• …and ${problems.length - 5} more', '• …以及另外 ${problems.length - 5} 个')

fs = F+'library/data/folder_scanner.dart'
add(fs, 'listing stalled (device unresponsive)', '列表读取停滞（设备无响应）')
add(fs, 'stat stalled (device unresponsive)', '属性读取停滞（设备无响应）')

tf = F+'metadata/data/template_file.dart'

# ---------- handoff ----------
cd = F+'handoff/presentation/contactsheet_dialog.dart'
add(cd, 'Access token (cs_pat_…)', '访问令牌（cs_pat_…）')
add(cd, '${flattenGalleryTree(_galleries!).length} galleries', '${flattenGalleryTree(_galleries!).length} 个画廊')
add(cd, 'Create a new gallery, or load existing ones.', '创建新画廊，或加载已有画廊。')
add(cd, 'Load the gallery the client reviewed.', '加载客户浏览过的画廊。')
add(cd, 'Load existing', '加载已有')
add(cd, 'New gallery…', '新建画廊…')
add(cd, 'Search galleries…', '搜索画廊…')
add(cd, 'No galleries match.', '没有匹配的画廊。')
add(cd, 'New gallery name…', '新画廊名称…')
add(cd, 'New gallery name', '新画廊名称')
add(cd, 'Nested sub-gallery', '嵌套子画廊')
add(cd, 'New sub-gallery', '新建子画廊')
add(cd, 'Send $count', '发送 $count')
add(cd, 'Pull marks', '拉取标记')
add(cd, 'Import collections as saved selections', '将收藏导入为已保存选择')

cc = F+'handoff/data/contactsheet_client.dart'
add(cc, 'Not authorised — check the token and its scopes', '未授权——请检查令牌及其权限范围')
add(cc, 'Not found — check the URL or gallery', '未找到——请检查 URL 或画廊')
add(cc, 'Server returned ${res.statusCode}', '服务器返回 ${res.statusCode}')
add(cc, 'Could not reach ContactSheet ($e)', '无法连接 ContactSheet（$e）')

td = F+'handoff/presentation/transfer_dialog.dart'
add(td, 'Move', '移动')
add(td, 'Copy', '复制')
add(td, "$verb $count photo${count == 1 ? '' : 's'}", '$verb $count 张照片')
add(td, '$verb ${widget.sources.length}', '$verb ${widget.sources.length} 张')
add(td, 'Include XMP sidecars', '包含 XMP 附属文件')
add(td, 'Subfolder (optional, e.g. selects)', '子文件夹（可选，如 selects）')

ts = F+'handoff/data/transfer_service.dart'

# ---------- delivery ----------
dd = F+'delivery/presentation/delivery_server_dialog.dart'
add(dd, 'Add server', '添加服务器')
add(dd, 'Edit server', '编辑服务器')
add(dd, 'Name (e.g. AP wire)', '名称（如 AP 通讯社）')
add(dd, 'Username (empty = anonymous)', '用户名（留空 = 匿名）')
add(dd, 'Accept self-signed certificate', '接受自签名证书')
add(dd, 'Private key file (empty = password auth)', '私钥文件（留空 = 密码认证）')
add(dd, 'Choose key file', '选择密钥文件')
add(dd, 'Key passphrase (empty = unencrypted key)', '密钥口令（留空 = 密钥未加密）')
add(dd, 'Remote folder (e.g. incoming/photos)', '远程文件夹（如 incoming/photos）')
add(dd, 'Test connection', '测试连接')
add(dd, 'Connection OK — logged in, folder reachable.', '连接正常——已登录，文件夹可访问。')

add(F+'delivery/domain/delivery_server.dart', 'FTPS (explicit TLS)', 'FTPS（显式 TLS）')

fc = F+'delivery/data/ftp_client.dart'
add(fc, 'Could not connect to $host:$port — $e', '无法连接 $host:$port——$e')
add(fc, 'TLS handshake with $host failed — $e', '与 $host 的 TLS 握手失败——$e')
add(fc, 'Data connection to $host:$dataPort failed — $e', '到 $host:$dataPort 的数据连接失败——$e')
add(fc, 'Could not parse the passive-mode reply from $host', '无法解析来自 $host 的被动模式回复')
add(fc, 'Malformed reply from $host: "$first"', '来自 $host 的异常回复：“$first”')
add(fc, '$host closed the connection', '$host 已关闭连接')
add(fc, '$host did not answer within ${timeout.inSeconds}s', '$host 在 ${timeout.inSeconds} 秒内未响应')
add(fc, '$host refused $step', '$host 拒绝了 $step')
add(fc, 'Could not create "$segment" on $host', '无法在 $host 上创建“$segment”')
add(fc, 'Server refused upload of "$remoteName"', '服务器拒绝了“$remoteName”的上传')
add(fc, 'transfer of $remoteName', '传输 $remoteName')

sc = F+'delivery/data/sftp_client.dart'
add(sc, 'Not connected', '未连接')
add(sc, '$host refused the login for "$username"', '$host 拒绝了用户“$username”的登录')
add(sc, 'Could not read the key "$keyFilePath" — $e', '无法读取密钥“$keyFilePath”——$e')
add(sc, 'Could not create "$path" on $host', '无法在 $host 上创建“$path”')
add(sc, 'Upload of "$remoteName" to $host failed — $e', '“$remoteName”上传到 $host 失败——$e')

# ---------- export ----------
xd = F+'export/presentation/export_dialog.dart'
add(xd, 'Choose a folder…', '选择文件夹…')
add(xd, 'Local folder', '本地文件夹')
add(xd, 'Upload to ${server.name} (${server.protocol.label})', '上传到 ${server.name}（${server.protocol.label}）')
add(xd, 'Same folder as originals', '与原文件同文件夹')
add(xd, 'Also keep a local copy', '同时保留本地副本')
add(xd, 'Exports (blank = alongside)', '导出位置（留空 = 与原文件同目录）')
add(xd, 'Open folder when done', '完成后打开文件夹')
add(xd, 'Size & quality', '尺寸与质量')
add(xd, 'Long edge', '长边')
add(xd, 'Custom…', '自定义…')
add(xd, 'Limit file size to', '限制文件大小为')
add(xd, 'Sharpen after resize', '缩放后锐化')
add(xd, "Export $count photo${count == 1 ? '' : 's'}", '导出 $count 张照片')
add(xd, 'e.g.  $_previewName', '例如  $_previewName')
add(xd, 'Export ${widget.sources.length}', '导出 ${widget.sources.length} 张')
add(xd, 'Export & upload ${widget.sources.length}', '导出并上传 ${widget.sources.length} 张')
add(xd, 'Exports', '导出')

# ---------- metadata domain ----------
ic = F+'metadata/domain/iptc_core.dart'
add(ic, 'Description', '说明')
add(ic, 'Location', '地点')
add(ic, 'Credit & rights', '署名与权利')
add(ic, 'Models & releases', '模特与授权')
add(ic, 'AI & provenance', 'AI 与来源信息')
add(ic, 'Caption', '说明文字')
add(ic, 'Headline', '标题')
add(ic, 'Date created', '创建日期')
add(ic, 'Title / Slug', '标题 / Slug')
add(ic, 'Alt text', '替代文本')
add(ic, 'Media topics', '媒体主题')
add(ic, 'Description writers', '说明撰写者')
add(ic, 'Persons shown', '画面人物')
add(ic, 'Featured org', '画面机构')
add(ic, 'Featured org code', '画面机构代码')
add(ic, 'Intellectual genre', '题材类型')
add(ic, 'IPTC scene', 'IPTC 场景')
add(ic, 'Event', '事件')
add(ic, 'Sublocation', '子地点')
add(ic, 'City', '城市')
add(ic, 'State / Province', '省州')
add(ic, 'Country', '国家')
add(ic, 'ISO code', 'ISO 代码')
add(ic, 'World region', '世界地区')
add(ic, 'Location ID', '地点 ID')
add(ic, 'Creator', '创作者')
add(ic, 'Job title', '职务')
add(ic, 'Creator email', '创作者邮箱')
add(ic, 'Creator website', '创作者网站')
add(ic, 'Creator address', '创作者地址')
add(ic, 'Creator city', '创作者城市')
add(ic, 'Creator state/region', '创作者省州')
add(ic, 'Creator postcode', '创作者邮编')
add(ic, 'Creator country', '创作者国家')
add(ic, 'Creator phone', '创作者电话')
add(ic, 'Credit', '署名')
add(ic, 'Copyright', '版权')
add(ic, 'Copyright status', '版权状态')
add(ic, 'Usage terms', '使用条款')
add(ic, 'Rights URL', '权利 URL')
add(ic, 'Instructions', '使用说明')
add(ic, 'Job ID / Transmission', '任务 ID / 传输')
add(ic, 'Image supplier', '图像供稿方')
add(ic, 'Supplier ID', '供稿方 ID')
add(ic, 'Supplier image ID', '供稿图像 ID')
add(ic, 'Category', '类别')
add(ic, 'Supplemental categories', '补充类别')
add(ic, 'Urgency', '紧急程度')
add(ic, 'Edit status', '编辑状态')
add(ic, 'Image GUID', '图像 GUID')
add(ic, 'Model release', '模特授权')
add(ic, 'Model release IDs', '模特授权 ID')
add(ic, 'Property release', '财产授权')
add(ic, 'Property release IDs', '财产授权 ID')
add(ic, 'Additional model info', '模特补充信息')
add(ic, 'Model age', '模特年龄')
add(ic, 'Minor model age disclosure', '未成年模特年龄披露')
add(ic, 'Source type', '来源类型')
add(ic, 'AI system', 'AI 系统')
add(ic, 'AI system version', 'AI 系统版本')
add(ic, 'AI prompt', 'AI 提示词')
add(ic, 'AI prompt writer', 'AI 提示词作者')

add(F+'metadata/domain/iptc_template.dart', 'Add to existing', '添加到现有内容')

tv = F+'metadata/domain/template_variables.dart'
add(tv, "Capture year, e.g. 2026 (today's if the photo has no date)", '拍摄年份，如 2026（照片无日期时用今天）')
add(tv, 'Capture month, 01–12', '拍摄月份，01–12')
add(tv, 'Capture day, 01–31', '拍摄日，01–31')
add(tv, 'Capture date, YYYY-MM-DD', '拍摄日期，YYYY-MM-DD')
add(tv, 'Capture time, HH:MM:SS', '拍摄时间，HH:MM:SS')
add(tv, 'File name with extension, e.g. DSC_0001.ARW', '含扩展名的文件名，如 DSC_0001.ARW')
add(tv, 'File name without extension, e.g. DSC_0001', '不含扩展名的文件名，如 DSC_0001')
add(tv, 'File extension without the dot, e.g. ARW', '不含点的扩展名，如 ARW')
add(tv, 'Camera model (blank if unknown)', '相机机型（未知时为空）')
add(tv, 'Lens model (blank if unknown)', '镜头型号（未知时为空）')
add(tv, 'Running number across the applied photos, starting at 1', '跨应用照片的流水号，从 1 开始')

add(F+'metadata/domain/template_snapshots.dart', 'Default', '默认')

# ---------- metadata presentation ----------
ed = F+'metadata/presentation/iptc_editor_dialog.dart'
add(ed, 'Stamp a metadata template onto the fields', '将元数据模板盖印到各字段')
add(ed, 'Name', '名称')
add(ed, 'Identifier', '标识符')
add(ed, 'Item ID', '条目 ID')
add(ed, 'Org ID', '机构 ID')
add(ed, 'Creator', '创作者')
add(ed, 'Source', '来源')
add(ed, 'Copyright', '版权')
add(ed, 'Sublocation', '子地点')
add(ed, 'City', '城市')
add(ed, 'Copy all IPTC fields (⌘/Ctrl+Shift+C)', '复制全部 IPTC 字段（⌘/Ctrl+Shift+C）')
add(ed, 'Paste copied IPTC fields (⌘/Ctrl+Shift+V)', '粘贴复制的 IPTC 字段（⌘/Ctrl+Shift+V）')
add(ed, 'Empty every field and table', '清空所有字段和表格')
add(ed, 'Could not load the template', '无法加载模板')
add(ed, 'Save as template', '另存为模板')
add(ed, 'Save as…', '另存为…')
add(ed, 'Save these fields as a named metadata template', '将这些字段保存为命名元数据模板')
add(ed, 'Editing $count photos — only fields you change are applied.', '正在编辑 $count 张照片——仅应用你修改的字段。')
add(ed, 'Next photo — saves edits (⌘/Ctrl+PgDn or ⌘/Ctrl+Enter)', '下一张——保存修改（⌘/Ctrl+PgDn 或 ⌘/Ctrl+Enter）')
add(ed, '${index + 1} of $total', '第 ${index + 1} / $total 张')
add(ed, 'Fill city/state/country from the photo’s GPS position', '根据照片的 GPS 位置填充城市/省州/国家')
add(ed, 'From GPS', '来自 GPS')
add(ed, 'This photo has no GPS position', '此照片没有 GPS 位置')
add(ed, 'From XMP file…', '来自 XMP 文件…')
add(ed, 'Clear (use capture time)', '清除（使用拍摄时间）')
add(ed, 'From capture time', '来自拍摄时间')
add(ed, 'Not set', '未设置')
add(ed, 'Mixed — leave to keep each photo’s value', '混合——保留各照片原值')
add(ed, 'Type to search the IPTC vocabulary…', '输入以搜索 IPTC 词汇…')
add(ed, '${topic.label}  ‹ ${topic.parent}', '${topic.label} ‹ ${topic.parent}')

tp = F+'metadata/presentation/iptc_template_dialog.dart'
add(tp, 'Metadata template', '元数据模板')
add(tp, 'Could not save the template', '无法保存模板')
add(tp, 'Copyright', '版权')
add(tp, 'Creator', '创作者')
add(tp, 'XMP templates', 'XMP 模板')
add(tp, 'Empty every field, keyword and table', '清空所有字段、关键字和表格')
add(tp, 'Load XMP…', '加载 XMP…')
add(tp, 'Save XMP…', '保存 XMP…')
add(tp, 'Load an XMP template file (Photo Mechanic / Bridge)', '加载 XMP 模板文件（Photo Mechanic / Bridge）')
add(tp, 'Save these values as an XMP template file', '将这些值保存为 XMP 模板文件')
add(tp, 'Recent values', '最近使用的值')
add(tp, 'Keywords', '关键字')

hd = F+'metadata/presentation/hot_codes_dialog.dart'
add(hd, 'Hot codes', '快捷代码')
add(hd, 'e.g. arena', '例如 arena')
add(hd, 'Add hot code', '添加快捷代码')
add(hd, 'Add field', '添加字段')
add(hd, 'Remove hot code', '删除快捷代码')
add(hd, 'Remove field', '移除字段')

cdt = F+'metadata/presentation/code_table_dialog.dart'
add(cdt, 'Code replacements', '代码替换')
add(cdt, 'Delimiter', '分隔符')
add(cdt, 'replacement  (alt1 | alt2)', '替换内容（候选1 | 候选2）')
add(cdt, 'Type text with a =code= to preview…', '输入含 =code= 的文本以预览…')
add(cdt, 'Add code', '添加代码')

add(F+'metadata/presentation/keyword_dialog.dart', 'Applies to ${widget.count} photos (replaces their keywords)', '应用到 ${widget.count} 张照片（替换其关键字）')
add(F+'metadata/presentation/keyword_dialog.dart', 'Comma-separated', '逗号分隔')
add(F+'metadata/presentation/keyword_dialog.dart', 'sunset, beach, portrait', '日落, 海滩, 人像')

add(F+'metadata/presentation/iptc_table_field.dart', 'Add row', '添加行')
add(F+'metadata/presentation/iptc_table_field.dart', 'Remove row', '删除行')

# ---------- naming ----------
ne = F+'naming/domain/name_element.dart'
add(ne, 'Date & time', '日期与时间')
add(ne, 'Date / time', '日期 / 时间')
add(ne, 'Date (2026-07-02)', '日期（2026-07-02）')
add(ne, 'Date (02.07.2026)', '日期（02.07.2026）')
add(ne, 'Date (02.07.26)', '日期（02.07.26）')
add(ne, 'Date (20260702)', '日期（20260702）')
add(ne, 'Year-month (2026-07)', '年月（2026-07）')
add(ne, 'Year (2026)', '年份（2026）')
add(ne, 'Month number (07)', '月份数字（07）')
add(ne, 'Month (Jul)', '月份（Jul）')
add(ne, 'Month (July)', '月份（July）')
add(ne, 'Weekday (Mon)', '星期（Mon）')
add(ne, 'Weekday (Monday)', '星期（Monday）')
add(ne, 'Time (143005)', '时间（143005）')
add(ne, 'Time (14-30)', '时间（14-30）')
add(ne, 'Job name', '任务名称')
add(ne, 'Counter', '计数器')
add(ne, 'Original filename', '原始文件名')
add(ne, 'Camera', '相机')
add(ne, 'Counter $w', '计数器（$w 位）')

npp = F+'naming/domain/name_preset.dart'
add(npp, 'Keep filenames', '保留文件名')
add(npp, 'Year / date_shoot / name', '年份 / 日期_拍摄 / 名称')
add(npp, 'Year / month / name', '年份 / 月 / 名称')
add(npp, 'Timestamped', '时间戳')

nb = F+'naming/presentation/name_builder.dart'
add(nb, 'Customise filename & folders', '自定义文件名与文件夹')
add(nb, 'Customise filename', '自定义文件名')
add(nb, 'Type here, or insert elements below…', '在此输入，或在下方插入元素…')
add(nb, 'Optional sub-folders, e.g. {YYYY}/{MM}', '可选子文件夹，如 {YYYY}/{MM}')
add(nb, 'Job name', '任务名称')
add(nb, 'Preset actions', '预设操作')
add(nb, 'Save as new preset…', '另存为新预设…')
add(nb, 'Save naming preset', '保存命名预设')
add(nb, "Delete '${selected.name}'", '删除“${selected.name}”')
add(nb, "$w digit${w == 1 ? '' : 's'}", '$w 位')
add(nb, 'e.g. Wedding-Anna (used by the Job-name element)', '如 Wedding-Anna（供 Job-name 元素使用）')

rd = F+'naming/presentation/rename_dialog.dart'
add(rd, 'Job name (the Job-name element)', '任务名称（Job-name 元素）')
add(rd, "Rename $count photo${count == 1 ? '' : 's'}", '重命名 $count 张照片')
add(rd, 'Rename ${widget.sources.length}', '重命名 ${widget.sources.length} 张')
add(rd, '…and ${widget.sources.length - 4} more', '…以及另外 ${widget.sources.length - 4} 张')

# ---------- settings ----------
sd = F+'settings/presentation/settings_dialog.dart'
add(sd, 'Performance', '性能')
add(sd, 'Interface', '界面')
add(sd, 'Ingest', '导入')
add(sd, 'Exposure brackets', '包围曝光')
add(sd, 'Metadata templates', '元数据模板')
add(sd, 'Startup', '启动')
add(sd, 'Delivery servers', '交付服务器')
add(sd, 'Send to editors', '发送到编辑器')
add(sd, 'Delivery', '交付')
add(sd, 'General', '常规')
add(sd, 'Reopen last folders on startup', '启动时重新打开上次文件夹')
add(sd, 'Check for updates on startup', '启动时检查更新')
add(sd, 'Clear thumbnail cache', '清除缩略图缓存')
add(sd, 'Thumbnail cache cleared', '缩略图缓存已清除')
add(sd, 'Show button tooltips', '显示按钮提示')
add(sd, 'Auto-advance to the next photo after rating or flagging', '评分或标记后自动跳到下一张')
add(sd, 'Flash a confirmation over the loupe when you mark a photo', '标记照片时在放大视图上闪烁确认')
add(sd, 'Apply ratings, flags and colours to the whole bracket', '将评分、标记和色标应用到整个包围曝光')
add(sd, 'Hot codes…', '快捷代码…')
add(sd, 'Code replacements…', '代码替换…')
add(sd, 'Set up template…', '设置模板…')
add(sd, 'New template', '新建模板')
add(sd, 'Edit "$name" (${_templateFieldCount()} fields)…', '编辑“$name”（${_templateFieldCount()} 个字段）…')
add(sd, 'Delete template', '删除模板')
add(sd, 'Apply to photos as they are ingested', '照片导入时应用')
add(sd, 'Add editor…', '添加编辑器…')
add(sd, 'Add server…', '添加服务器…')
add(sd, 'Remove server', '删除服务器')
add(sd, 'View logs', '查看日志')
add(sd, 'About & licenses', '关于与许可')
add(sd, 'Cullimingo · Version $kAppVersion', 'Cullimingo · 版本 $kAppVersion')
add(sd, 'Applies the next time you start Cullimingo.', '在下次启动 Cullimingo 时生效。')

add(F+'settings/presentation/performance_preset_selector.dart', 'Recommended', '推荐')

dg = F+'settings/presentation/diagnostics.dart'
add(dg, 'Cullimingo Logs', 'Cullimingo 日志')

# ---------- shared ----------
add(S+'widgets/dialog_kit.dart', 'Choose…', '选择…')
add(S+'widgets/dialog_kit.dart', 'Customer / assignment name', '客户 / 任务名称')


# ---- residual sweep round 2 ----
add(jr, '${summary.failed} failed', '${summary.failed} 个失败')
add(jr, 'Retry failed', '重试失败项')
add(F+'cull/presentation/widgets/cull_toolbar.dart', 'Rotate left', '向左旋转')
add(F+'cull/presentation/widgets/cull_toolbar.dart', 'Rotate right', '向右旋转')
add(F+'cull/presentation/widgets/photo_cell.dart', 'Rotate left', '向左旋转')
add(F+'cull/presentation/widgets/photo_cell.dart', 'Rotate right', '向右旋转')
add(tb, 'Edit metadata (M)', '编辑元数据（M）')
add(F+'cull/presentation/widgets/find_similar_dialog.dart', 'Find similar photos', '查找相似照片')
add(kd, 'Keyboard shortcuts', '键盘快捷键')
add(kd, 'Move between photos', '在照片间移动')
add(ke, 'Press a key for “${_armed!.label}” (Esc to cancel)', '为“${_armed!.label}”按一个键（Esc 取消）')
add(pc, 'Edit metadata', '编辑元数据')
add(tm, '$count photos', '$count 张照片')
add(tm, 'Apply metadata template', '应用元数据模板')
add(tm, 'Fill location from GPS', '从 GPS 填充位置')
add(cd, 'Renders JPEGs (in-camera look) and uploads them to the gallery.', '渲染 JPEG（机内观感）并上传到画廊。')
add(cd, 'Size & quality', '尺寸与质量')
add(td, 'Choose a folder…', '选择文件夹…')
add(td, 'Open folder when done', '完成后打开文件夹')
add(F+'metadata/data/template_file.dart', 'This XMP file contains no template fields — nothing to load.', '此 XMP 文件不包含模板字段——没有可加载的内容。')
add(ed, 'Date created', '创建日期')
add(ed, 'Image creators', '图像创作者')
add(ed, 'Locations shown', '所示地点')
add(ed, 'Registry entries', '注册条目')
add(ed, 'World region', '世界地区')
add(tp, 'Could not load the template', '无法加载模板')
add(tp, 'Image creators', '图像创作者')
add(tp, 'Locations shown', '所示地点')
add(tp, 'Registry entries', '注册条目')
add(tp, 'World region', '世界地区')
add(nb, 'Preset name', '预设名称')
add(sd, 'Code replacements (${_codes.codes.length})…', '代码替换（${_codes.codes.length}）…')
add(sd, 'Hot codes (${_hotCodes.codes.length})…', '快捷代码（${_hotCodes.codes.length}）…')
add(sd, 'Access token (cs_pat_…)', '访问令牌（cs_pat_…）')
add(sd, 'Edit server', '编辑服务器')
add(sd, 'No saved templates', '没有已保存模板')
add(sd, 'Open Import automatically when a memory card is inserted', '插入存储卡时自动打开导入')
add(sd, 'Rename template', '重命名模板')
add(sc, 'Could not connect to $host:$port — $e', '无法连接 $host:$port——$e')
add(fc, 'Connection to $host — $error', '到 $host 的连接——$error')
add(lv, 'Show info (I)', '显示信息（I）')
add(lv, 'Hide info (I)', '隐藏信息（I）')


# ---- residual sweep round 3 ----
add(tm, 'Rename…', '重命名…')
add(cd, 'Long edge', '长边')
add(ip, 'Hide inspector (I)', '隐藏检查器（I）')
add(ed, 'Artwork or object', '艺术品或对象')
add(ed, 'Copyright owners', '版权所有者')
add(ed, 'Country', '国家')
add(ed, 'Location', '地点')
add(ed, 'Location ID', '地点 ID')
add(ed, 'Media topics', '媒体主题')
add(ed, 'XMP templates', 'XMP 模板')
add(tp, 'Artwork or object', '艺术品或对象')
add(tp, 'Copyright owners', '版权所有者')
add(tp, 'Country', '国家')
add(tp, 'Identifier', '标识符')
add(tp, 'Item ID', '条目 ID')
add(tp, 'Org ID', '机构 ID')
add(tp, 'Location', '地点')
add(tp, 'Location ID', '地点 ID')
add(tp, 'XMP templates', 'XMP 模板')
add(nb, 'Elements', '元素')
cm = S+'models/cull_marks.dart'
add(cm, 'None', '无')
add(cm, 'Red', '红')
add(cm, 'Yellow', '黄')
add(cm, 'Green', '绿')
add(cm, 'Blue', '蓝')
add(cm, 'Purple', '紫')

# ---------- concat groups: (file, old_combined, new_text) ----------
SPANS = [
 (dg, 'A fast, cross-platform photo culling app. Ingest, cull, filter, export, hand off — speed is the product.',
      '一款快速的跨平台照片筛选应用。导入、筛选、过滤、导出、移交——速度即产品。'),
 (sd, 'Expand pulled-in client picks (Find / ContactSheet) to their brackets automatically',
      '把拉取的客户精选（查找 / ContactSheet）自动扩展到其包围曝光'),
 (sd, 'Caption, credit, location… to stamp onto photos, saved as named templates you can switch per customer or assignment. Use {year}/{name}/{camera}… variables and =code= replacements; the active template applies with the ⋮ menu, T, or automatically on ingest.',
      '要盖印到照片上的说明、署名、地点…，保存为可按客户或任务切换的命名模板。可使用 {year}/{name}/{camera}… 变量和 =code= 替换；活动模板通过 ⋮ 菜单、T 键或导入时自动应用。'),
 (sd, 'Hand the selected photos to another app from the right-click menu; the first editor is ⌘E.',
      '从右键菜单把所选照片交给其他应用；第一个编辑器为 ⌘E。'),
 (sd, 'FTP/FTPS/SFTP destinations the export dialog can upload to (wire/agency delivery). Passwords are stored in the system keychain, not in the settings file.',
      '导出对话框可上传到的 FTP/FTPS/SFTP 目标（通讯社/机构交付）。密码保存在系统钥匙串中，而非设置文件。'),
 (jr, 'Found ${result.burstCount} similar group(s), ${result.memberIds.length} photos · ${sensitivity.label} (Similar filter)',
      '找到 ${result.burstCount} 个相似组、${result.memberIds.length} 张照片 · ${sensitivity.label}（相似筛选）'),
 (F+'cull/presentation/cull_page.dart', "$n ${n == 1 ? 'mark' : 'marks'} saved, but the .xmp sidecar couldn't be written — check the folder is writable.",
      '$n 条标记已保存，但 .xmp 附属文件无法写入——请检查文件夹是否可写。'),
 (cj, "Opening ${paths.length} photo${paths.length == 1 ? '' : 's'} in ${editor.label}",
      '正在 ${editor.label} 中打开 ${paths.length} 张照片'),
 (sl, 'Selected ${ids.length} of ${list.filenames.length} from ${file.name}${_bracketSuffix(ids, selected)}',
      '已从 ${file.name} 中选中 ${ids.length} / ${list.filenames.length} 张${_bracketSuffix(ids, selected)}'),
 (sl, 'Selected ${ids.length} of ${names.length} name(s)${_bracketSuffix(ids, selected)}',
      '已从 ${names.length} 个名称中选中 ${ids.length} 张${_bracketSuffix(ids, selected)}'),
 (sl, 'When a name has both a RAW and a JPEG, select just the RAW. A JPEG with no RAW twin is still selected.',
      '当同一文件名同时有 RAW 和 JPEG 时，只选择 RAW。没有对应 RAW 的 JPEG 仍会被选中。'),
 (sl, 'Paste a list of filenames (from Capture One, Lightroom or ContactSheet). Any separator works, and the extension is optional — a JPEG list still selects your RAWs.',
      '粘贴文件名列表（来自 Capture One、Lightroom 或 ContactSheet）。分隔符不限，扩展名可省略——JPEG 列表同样能选中你的 RAW。'),
 (wsp, "Filled location on ${outcome.filled} photo(s)${skipped.isEmpty ? '' : ' · $skipped'}",
      "已为 ${outcome.filled} 张照片填充位置${skipped.isEmpty ? '' : ' · $skipped'}"),
 (wsp, "Can't refresh: the folder is missing or empty — is the card or drive connected? Nothing was removed.",
      '无法刷新：文件夹缺失或为空——存储卡或驱动器是否已连接？未删除任何内容。'),
 (wsp, "Refreshed: +${result.added} photo(s), but ${result.unreadable} item(s) in the folder couldn't be read — nothing was removed. Check the card or drive and its permissions.",
      '已刷新：+${result.added} 张照片，但 ${result.unreadable} 个项目无法读取——未删除任何内容。请检查存储卡或驱动器及其权限。'),
 (wsp, "Refreshed: +${result.added} / −${result.removed} photo(s)${result.changedPaths.isEmpty ? '' : ' · '\n                          '${result.changedPaths.length} changed'}",
      "已刷新：+${result.added} / −${result.removed} 张${result.changedPaths.isEmpty ? '' : ' · ${result.changedPaths.length} 张有改动'}"),
 (wsp, "${parts.isEmpty ? '' : ' · '}${scan.unreadable} item(s) couldn't be read",
      "${parts.isEmpty ? '' : ' · '}${scan.unreadable} 个项目无法读取"),
 (dr, 'Move $count $descriptor to the Trash?\\n\\nThe originals and their .xmp sidecars leave this folder. Nothing is permanently deleted — you can restore them from the Trash.',
      '将 $count $descriptor 移到废纸篓？\n\n原图及其 .xmp 附属文件将离开此文件夹。不会永久删除——可从废纸篓恢复。'),
 (kd, 'Press ? any time for the full list — and rebind anything under Settings.',
      '随时按 ? 查看完整列表——所有快捷键可在设置中重新绑定。'),
 (ke, '“${keyDisplayLabel(key)}” is reserved for navigation and can’t be assigned.',
      '“${keyDisplayLabel(key)}”保留给导航，无法分配。'),
 (ke, '“${keyDisplayLabel(key)}” is already used by “${clash.label}”.',
      '“${keyDisplayLabel(key)}”已被“${clash.label}”使用。'),
 (ke, 'Click a key to rebind it. Arrows, Esc, Enter and the ⌘/Ctrl combos stay fixed.',
      '点击按键即可重新绑定。方向键、Esc、Enter 和 ⌘/Ctrl 组合键固定不变。'),
 (ip, 'Cropped (LR) · ${formatCrop(d.crop!.width, d.crop!.height, d.crop!.angle)}',
      '已在 LR 中裁剪 · ${formatCrop(d.crop!.width, d.crop!.height, d.crop!.angle)}'),
 (ts, "Photo copied, but its sidecar wasn't: ${sidecarResult.message ?? sidecarResult.outcome.name}",
      '照片已复制，但其附属文件未复制：${sidecarResult.message ?? sidecarResult.outcome.name}'),
 (cd, 'Fetches client ratings + colours and applies them to the matching photos by filename (selecting the ones the client marked).',
      '按文件名拉取客户评分 + 色标并应用到匹配的照片（即客户标记的那些）。'),
 (td, 'Move copies the originals to the destination and removes them from their current folder — only after each copy is verified.',
      '移动会把原文件复制到目标位置，并在每次复制校验通过后才将其从当前文件夹移除。'),
 (td, 'Copy duplicates the originals; the files stay where they are.',
      '复制会生成原文件的副本；原文件保留在原处。'),
 (ig, 'That looks like a whole drive. Choose a folder on it with Browse… (or insert a camera card) to scan.',
      '这看起来是整个驱动器。用「浏览…」选择其中的一个文件夹（或插入相机存储卡）以扫描。'),
 (ig, "$n ${n == 1 ? 'item' : 'items'} on the source couldn't be read and won't be imported. Don't format the card until you've checked it.",
      '来源上的 $n 个项目无法读取，不会被导入。确认检查完成前请勿格式化存储卡。'),
 (ig, 'Copying ${pr.done} / ${pr.total}  ·  ${_speed(pr)}  —  ${p.basename(pr.last.source)}',
      '正在复制 ${pr.done} / ${pr.total} · ${_speed(pr)} — ${p.basename(pr.last.source)}'),
 (ig, "Part of the source couldn't be read, so its files weren't imported. Don't format the card until you've checked it.",
      '部分来源无法读取，其中的文件未被导入。确认检查完成前请勿格式化存储卡。'),
 (ig, '${plan.items.length} photos · ${_formatBytes(plan.totalBytes)}',
      '${plan.items.length} 张照片 · ${_formatBytes(plan.totalBytes)}'),
 (rd, 'Renames the files in place (with their .xmp sidecars). Name clashes get a _2, _3… suffix.',
      '就地重命名文件（连同 .xmp 附属文件）。名称冲突会自动加 _2、_3… 后缀。'),
 (dd, 'Plain FTP sends the password unencrypted — fine on a LAN/VPN, avoid on the open internet.',
      '明文 FTP 会未加密地传输密码——在局域网/专用网络中可用，公开互联网上请勿使用。'),
 (fb, 'Needs caption (${count((p) => p.iptc.caption.trim().isEmpty)})',
      '缺说明（${count((p) => p.iptc.caption.trim().isEmpty)}）'),
 (xd, 'Embedded-preview export — the in-camera look (great for proofs/web), not a Capture One / Lightroom render.',
      '嵌入式预览导出——机内观感（适合样片/网络），不是 Capture One / Lightroom 的渲染结果。'),
 (F+'metadata/data/template_file.dart', 'The file could not be opened. Check that it still exists and is readable.',
      '无法打开该文件。请检查它是否仍存在且可读。'),
 (F+'metadata/data/template_file.dart', 'This is not an XMP template. Choose a .xmp file saved from a metadata template — by Photo Mechanic, Adobe Bridge, or Cullimingo.',
      '这不是 XMP 模板。请选择由元数据模板保存的 .xmp 文件——来自 Photo Mechanic、Adobe Bridge 或 Cullimingo。'),
 (F+'metadata/data/template_file.dart', 'The file could not be written. Check that the folder exists and is writable.',
      '无法写入该文件。请检查文件夹是否存在且可写。'),
 (cdt, 'Type a code between the delimiter (e.g. =ff=) in any template field and it expands to its text. Separate alternates with “ | ” — =ff#2= picks the second.',
      '在任意模板字段的分隔符之间输入代码（如 =ff=）即展开为其文本。用“ | ”分隔候选——=ff#2= 选择第二个。'),
 (hd, 'A hot code fills several metadata fields at once: type its =code= in any Metadata-editor field and every field below is stamped (the field you typed in keeps its other text). Values may use =text codes= and {variables}. Uses the same delimiter as the code replacements.',
      '一个快捷代码可同时填充多个元数据字段：在任意元数据编辑字段中输入其 =code=，下方每个字段都会被盖印（你输入的字段保留其余文本）。值可以使用 =文本代码= 和 {变量}。与代码替换使用相同的分隔符。'),
 (ed, 'Previous photo — saves edits (⌘/Ctrl+PgUp or ⌘/Ctrl+Shift+Enter)',
      '上一张——保存修改（⌘/Ctrl+PgUp 或 ⌘/Ctrl+Shift+Enter）'),
 (tp, 'Tick the fields to stamp onto photos. Unticked fields are left untouched. Use {year} {date} {name} {camera} variables and =code= replacements — they expand per photo when applied.',
      '勾选要盖印到照片上的字段。未勾选的字段保持原样。可使用 {year} {date} {name} {camera} 变量和 =code= 替换——应用时会按每张照片展开。'),
]
