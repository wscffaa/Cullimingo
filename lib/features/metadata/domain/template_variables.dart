import 'package:path/path.dart' as p;

/// The template variables Cullimingo understands, with a short description for
/// the editor's insert menu. We use readable `{token}` names rather than Photo
/// Mechanic's cryptic `%`/`{}` codes — the whole point of "better than PM".
const Map<String, String> kTemplateVariableHelp = {
  'year': "拍摄年份，如 2026（照片无日期时用今天）",
  'month': '拍摄月份，01–12',
  'day': '拍摄日，01–31',
  'date': '拍摄日期，YYYY-MM-DD',
  'time': '拍摄时间，HH:MM:SS',
  'filename': '含扩展名的文件名，如 DSC_0001.ARW',
  'name': '不含扩展名的文件名，如 DSC_0001',
  'ext': '不含点的扩展名，如 ARW',
  'camera': '相机机型（未知时为空）',
  'lens': '镜头型号（未知时为空）',
  'seq': '跨应用照片的流水号，从 1 开始',
};

/// Builds the `{token}` → value map for one photo. Date tokens fall back to the
/// current date when the photo has no capture time, so `{year}` in a copyright
/// notice always resolves. Unknown/blank fields are simply omitted (then
/// [expandVariables] leaves their token untouched).
Map<String, String> templateVariables({
  required String path,
  DateTime? capturedAt,
  String? camera,
  String? lens,
  int? sequence,
}) {
  final dt = capturedAt ?? DateTime.now();
  String two(int n) => n.toString().padLeft(2, '0');
  return {
    'year': '${dt.year}',
    'month': two(dt.month),
    'day': two(dt.day),
    'date': '${dt.year}-${two(dt.month)}-${two(dt.day)}',
    'time': '${two(dt.hour)}:${two(dt.minute)}:${two(dt.second)}',
    'filename': p.basename(path),
    'name': p.basenameWithoutExtension(path),
    'ext': p.extension(path).replaceFirst('.', ''),
    if (camera != null && camera.isNotEmpty) 'camera': camera,
    if (lens != null && lens.isNotEmpty) 'lens': lens,
    if (sequence != null) 'seq': '$sequence',
  };
}

/// Replaces every `{token}` in [input] with its value from [vars]. An unknown
/// token is left exactly as written (non-destructive), so a literal `{foo}`
/// survives and a typo is visible rather than silently blanked.
String expandVariables(String input, Map<String, String> vars) =>
    input.replaceAllMapped(RegExp(r'\{(\w+)\}'), (match) {
      final token = match.group(1)!;
      return vars[token] ?? match.group(0)!;
    });

/// Photo Mechanic variable names (long and 4-char short form, lowercase — PM
/// matches its variables case-insensitively) → the Cullimingo token(s) with
/// the same meaning, brace-wrapped and ready to splice in. PM's `{datesort}`
/// (YYYYMMDD) has no single token here, so it maps to a composite. PM names
/// with no exact equivalent (`{hour24}`, `{iptccity}`, …) are deliberately
/// absent: they survive translation literally, so the user sees them in the
/// editor instead of getting silently wrong values. Note PM's `{lens}` is the
/// focal length — its lens *name* variable is `{lenstype}`, which is what our
/// `{lens}` means. Same-named same-meaning variables (`{filename}`, `{time}`)
/// need no entry.
const Map<String, String> kPhotoMechanicVariables = {
  'file': '{filename}',
  'filenamebase': '{name}',
  'fbas': '{name}',
  'year4': '{year}',
  'yr4': '{year}',
  'month0': '{month}',
  'mn0': '{month}',
  'day0': '{day}',
  'datesort': '{year}{month}{day}',
  'dats': '{year}{month}{day}',
  'model': '{camera}',
  'modl': '{camera}',
  'lenstype': '{lens}',
  'lt': '{lens}',
  'sequence': '{seq}',
  'seqn': '{seq}',
  'auto': '{seq}',
};

/// Rewrites Photo Mechanic `{variables}` in [input] into their Cullimingo
/// `{token}` equivalents via [kPhotoMechanicVariables], so a template saved by
/// PM keeps working when applied here. Anything unrecognised — including our
/// own tokens, which share no name with a PM alias — passes through unchanged,
/// making the rewrite a safe no-op on Cullimingo-written files.
String translatePmVariables(String input) => input.replaceAllMapped(
  RegExp(r'\{(\w+)\}'),
  (match) =>
      kPhotoMechanicVariables[match.group(1)!.toLowerCase()] ?? match.group(0)!,
);
