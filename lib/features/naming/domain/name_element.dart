/// The catalog behind the naming builder's "Elements" palette: it describes the
/// tokens a user can insert, their labels, and which per-element option a token
/// carries (counter width, date format) — offered as a small dropdown menu.
///
/// This is the single source of truth: the palette is built from
/// [paletteGroups], with [counterWidths] and [dateFormats] backing the counter
/// and date menus. Adding a resolvable EXIF token later is a data-only change.
library;

/// The per-chip option a token carries — mirrors Capture One's dropdowns.
enum NameOption {
  /// No options (a plain token).
  none,

  /// A counter (`seq:N`) with a digit-width dropdown.
  counter,

  /// A date/time (`date:key`) with a format dropdown.
  date,
}

/// One insertable palette element (a button in a "Gruppe").
class NameElement {
  /// Creates a palette element.
  const NameElement({
    required this.label,
    required this.token,
    this.option = NameOption.none,
  });

  /// Button label in the palette.
  final String label;

  /// The token body inserted (no braces), e.g. `origname`, `seq:3`, `date:iso`.
  final String token;

  /// Which per-chip option (if any) this element exposes once inserted.
  final NameOption option;
}

/// A titled group of palette elements (Capture One's "Gruppe").
class NameElementGroup {
  /// Creates a group.
  const NameElementGroup(this.title, this.elements);

  /// Group heading.
  final String title;

  /// The elements in the group.
  final List<NameElement> elements;
}

/// The counter widths offered by the counter chip's dropdown (1–6 digits).
const List<int> counterWidths = [1, 2, 3, 4, 5, 6];

/// The date/time formats offered by the date chip's dropdown, in menu order,
/// each `date:` key paired with a human label + hint (Capture One shows the
/// pattern hint, e.g. "Aktuelles Datum (MMM tt jjjj)").
const List<({String key, String label})> dateFormats = [
  (key: 'iso', label: '日期（2026-07-02）'),
  (key: 'dmyDots', label: '日期（02.07.2026）'),
  (key: 'dmyDotsShort', label: '日期（02.07.26）'),
  (key: 'compact', label: '日期（20260702）'),
  (key: 'yearMonth', label: '年月（2026-07）'),
  (key: 'year', label: '年份（2026）'),
  (key: 'monthNumber', label: '月份数字（07）'),
  (key: 'monthName', label: '月份（Jul）'),
  (key: 'monthNameFull', label: '月份（July）'),
  (key: 'monthDayYear', label: 'Jul 02 2026'),
  (key: 'dayMonthYear', label: '02 Jul 2026'),
  (key: 'weekday', label: '星期（Mon）'),
  (key: 'weekdayFull', label: '星期（Monday）'),
  (key: 'time', label: '时间（143005）'),
  (key: 'timeHM', label: '时间（14-30）'),
];

/// The palette, grouped like Capture One's element list. Only tokens the engine
/// can actually resolve today are offered; the catalog is data-driven so more
/// plug in without touching the builder UI.
const List<NameElementGroup> paletteGroups = [
  NameElementGroup('Job', [
    NameElement(label: '任务名称', token: 'shoot'),
    NameElement(label: '计数器', token: 'seq:3', option: NameOption.counter),
  ]),
  NameElementGroup('日期与时间', [
    NameElement(
      label: '日期 / 时间',
      token: 'date:iso',
      option: NameOption.date,
    ),
  ]),
  NameElementGroup('File', [
    NameElement(label: '原始文件名', token: 'origname'),
    NameElement(label: '相机', token: 'camera'),
  ]),
];

/// Friendly display label for each engine token. The naming fields show a
/// readable `{Original filename}` / `{Counter 3}` / `{Date (2026-07-02)}`
/// instead of the raw `{origname}` / `{seq:3}` / `{date:iso}` engine tokens;
/// [engineToDisplay] / [displayToEngine] bridge the two. The map is bijective
/// over the tokens the palette can produce, so the round-trip is lossless.
final Map<String, String> tokenDisplayLabels = {
  'shoot': '任务名称',
  'origname': '原始文件名',
  'camera': '相机',
  'seq': '计数器',
  for (final w in counterWidths) 'seq:$w': '计数器（$w 位）',
  for (final f in dateFormats) 'date:${f.key}': f.label,
};

final Map<String, String> _displayToToken = {
  for (final e in tokenDisplayLabels.entries) e.value: e.key,
};

final RegExp _brace = RegExp(r'\{([^}]+)\}');

/// The friendly display token (e.g. `{Original filename}`) for an engine
/// [token], for inserting into a naming field.
String displayTokenFor(String token) =>
    '{${tokenDisplayLabels[token] ?? token}}';

/// Rewrites an engine pattern into the friendly text shown in a naming field.
/// Unknown tokens (e.g. a hand-typed one) pass through unchanged.
String engineToDisplay(String pattern) => pattern.replaceAllMapped(
  _brace,
  (m) => '{${tokenDisplayLabels[m[1]!] ?? m[1]!}}',
);

/// Rewrites friendly field text back into an engine pattern. Free-typed literal
/// text (anything not inside `{…}`) and unknown `{…}` pass through unchanged.
String displayToEngine(String display) => display.replaceAllMapped(
  _brace,
  (m) => '{${_displayToToken[m[1]!] ?? m[1]!}}',
);
