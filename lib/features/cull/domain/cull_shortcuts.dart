import 'package:flutter/services.dart';

/// A rebindable cull/view action (`BUILD_PLAN.md` §7/§8 — configurable keymap).
/// Navigation (arrows), overlay keys (Esc, Enter, `[`/`]`) and the ⌘/Ctrl
/// app combos are intentionally NOT here — they stay fixed.
enum CullAction {
  /// Flag as pick.
  pick('精选', LogicalKeyboardKey.keyP),

  /// Flag as reject.
  reject('剔除', LogicalKeyboardKey.keyX),

  /// Clear the rating. `0` matches the de-facto culling standard (Photo
  /// Mechanic, Lightroom, Capture One all clear/zero a rating with `0`); Delete
  /// stays a fixed secondary.
  clearRating('清除星级', LogicalKeyboardKey.digit0),

  /// Rate 1 star.
  rate1('评 1 星', LogicalKeyboardKey.digit1),

  /// Rate 2 stars.
  rate2('评 2 星', LogicalKeyboardKey.digit2),

  /// Rate 3 stars.
  rate3('评 3 星', LogicalKeyboardKey.digit3),

  /// Rate 4 stars.
  rate4('评 4 星', LogicalKeyboardKey.digit4),

  /// Rate 5 stars.
  rate5('评 5 星', LogicalKeyboardKey.digit5),

  /// Colour label red.
  colorRed('色标：红', LogicalKeyboardKey.digit6),

  /// Colour label yellow.
  colorYellow('色标：黄', LogicalKeyboardKey.digit7),

  /// Colour label green.
  colorGreen('色标：绿', LogicalKeyboardKey.digit8),

  /// Colour label blue.
  colorBlue('色标：蓝', LogicalKeyboardKey.digit9),

  /// Colour label purple. Purple is the odd colour out across cullers (none
  /// give it a number key), so it parks on Backspace, freed by clear-rating
  /// moving to `0`.
  colorPurple('色标：紫', LogicalKeyboardKey.backspace),

  /// Toggle the photo in the selection.
  select('选择', LogicalKeyboardKey.space),

  /// Open / close the loupe.
  loupe('放大视图', LogicalKeyboardKey.keyF),

  /// Compare the selection.
  compare('对比已选', LogicalKeyboardKey.keyC),

  /// Compare the focused photo's group.
  compareBurst("对比焦点照片的组", LogicalKeyboardKey.keyB),

  /// Toggle the info inspector.
  inspector('信息检查器', LogicalKeyboardKey.keyI),

  /// Edit keywords.
  keywords('编辑关键字', LogicalKeyboardKey.keyK),

  /// Edit IPTC metadata (caption, creator, credit, location…).
  metadata('编辑元数据', LogicalKeyboardKey.keyM),

  /// Stamp the saved metadata template onto the selection/focused photo. `T`
  /// for template — plain T is free (⌘/Ctrl+T is new-tab, checked before the
  /// cull keys).
  applyTemplate('应用元数据模板', LogicalKeyboardKey.keyT),

  /// Rename the selection in place. `R` for rename — plain R is free
  /// (⌘/Ctrl+R is refresh-folder, checked before the cull keys). Photo
  /// Mechanic uses M, but M is already Edit-metadata here; rebindable anyway.
  rename('重命名…', LogicalKeyboardKey.keyR),

  /// Rotate the selection 90° clockwise. `.` (period) — the `[`/`]` keys that
  /// Lightroom uses are reserved here for loupe zoom, so rotate parks on the
  /// adjacent `,`/`.` pair. Rebindable.
  rotateRight('向右旋转', LogicalKeyboardKey.period),

  /// Rotate the selection 90° counter-clockwise. `,` (comma) — see
  /// [rotateRight].
  rotateLeft('向左旋转', LogicalKeyboardKey.comma),

  /// Grow the selection to include every frame of each selected photo's
  /// exposure bracket (its ±EV siblings). `G` for group — free across the
  /// keymap. Rebindable.
  expandBrackets('扩展选择到包围曝光', LogicalKeyboardKey.keyG);

  const CullAction(this.label, this.defaultKey);

  /// Human-readable action name.
  final String label;

  /// The default key for this action.
  final LogicalKeyboardKey defaultKey;
}

/// Human-readable label for a key (`P`, `Space`, `Backspace`, `6`, …) for the
/// shortcuts UI.
String keyDisplayLabel(LogicalKeyboardKey key) {
  final named = _namedKeys[key];
  if (named != null) return named;
  final label = key.keyLabel;
  return label.isNotEmpty ? label.toUpperCase() : (key.debugName ?? 'Key');
}

final Map<LogicalKeyboardKey, String> _namedKeys = {
  LogicalKeyboardKey.space: '空格',
  LogicalKeyboardKey.backspace: '退格',
  LogicalKeyboardKey.delete: '删除',
  LogicalKeyboardKey.enter: '回车',
  LogicalKeyboardKey.tab: 'Tab',
  LogicalKeyboardKey.arrowLeft: '←',
  LogicalKeyboardKey.arrowRight: '→',
  LogicalKeyboardKey.arrowUp: '↑',
  LogicalKeyboardKey.arrowDown: '↓',
  LogicalKeyboardKey.bracketLeft: '[',
  LogicalKeyboardKey.bracketRight: ']',
};

/// The resolved cull keymap: every [CullAction] mapped to a key, defaults
/// overlaid with the user's rebindings. Pure and immutable.
class CullShortcuts {
  /// Wraps a complete action→key map.
  const CullShortcuts(this._bindings);

  /// The default keymap.
  factory CullShortcuts.defaults() => CullShortcuts({
    for (final a in CullAction.values) a: a.defaultKey,
  });

  /// Builds from persisted [overrides] (action name → key id), falling back to
  /// defaults for anything unset or unknown.
  factory CullShortcuts.fromOverrides(Map<String, int> overrides) {
    final map = {for (final a in CullAction.values) a: a.defaultKey};
    final byName = {for (final a in CullAction.values) a.name: a};
    overrides.forEach((name, keyId) {
      final action = byName[name];
      if (action != null) map[action] = LogicalKeyboardKey(keyId);
    });
    return CullShortcuts(map);
  }

  final Map<CullAction, LogicalKeyboardKey> _bindings;

  /// Keys that may NOT be assigned to an action (they drive fixed navigation /
  /// overlay behaviour).
  static final Set<LogicalKeyboardKey> reservedKeys = {
    LogicalKeyboardKey.arrowLeft,
    LogicalKeyboardKey.arrowRight,
    LogicalKeyboardKey.arrowUp,
    LogicalKeyboardKey.arrowDown,
    LogicalKeyboardKey.escape,
    LogicalKeyboardKey.enter,
    LogicalKeyboardKey.tab,
    LogicalKeyboardKey.bracketLeft,
    LogicalKeyboardKey.bracketRight,
  };

  /// Whether [key] can be bound to an action.
  static bool isAssignable(LogicalKeyboardKey key) =>
      !reservedKeys.contains(key);

  /// The key bound to [action].
  LogicalKeyboardKey keyFor(CullAction action) => _bindings[action]!;

  /// The action bound to [key], or null if none.
  CullAction? actionFor(LogicalKeyboardKey key) {
    for (final entry in _bindings.entries) {
      if (entry.value == key) return entry.key;
    }
    return null;
  }

  /// The *other* action already bound to [key] (a conflict if [action] were
  /// rebound to it), or null if [key] is free.
  CullAction? conflictFor(CullAction action, LogicalKeyboardKey key) {
    for (final entry in _bindings.entries) {
      if (entry.key != action && entry.value == key) return entry.key;
    }
    return null;
  }

  /// Returns a copy with [action] rebound to [key].
  CullShortcuts withBinding(CullAction action, LogicalKeyboardKey key) =>
      CullShortcuts({..._bindings, action: key});

  /// The non-default bindings, as `actionName → keyId`, for persistence.
  Map<String, int> toOverrides() => {
    for (final entry in _bindings.entries)
      if (entry.value != entry.key.defaultKey)
        entry.key.name: entry.value.keyId,
  };
}
