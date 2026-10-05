import 'package:cullimingo/app/theme/tokens.dart';
import 'package:cullimingo/features/metadata/domain/code_replacements.dart';
import 'package:cullimingo/shared/widgets/dialog_kit.dart';
import 'package:flutter/material.dart';

/// Joins a code's alternates for the single editor field
/// (e.g. `staff | Jane Smith`).
String _joinAlternates(List<String> replacements) => replacements.join(' | ');

/// Splits the editor field back into alternates, dropping blanks.
List<String> _splitAlternates(String text) => [
  for (final part in text.split('|'))
    if (part.trim().isNotEmpty) part.trim(),
];

/// Opens the code-replacement table editor seeded from [initial]; returns the
/// edited table or null if cancelled.
Future<CodeReplacements?> showCodeTableEditor(
  BuildContext context, {
  required CodeReplacements initial,
}) => showDialog<CodeReplacements>(
  context: context,
  // A form — an outside click must not discard the codes being edited.
  barrierDismissible: false,
  builder: (_) => CodeTableDialog(initial: initial),
);

/// The in-app code-replacement table: rows of `code → replacements` (alternates
/// separated by ` | `, so `=ff=` / `=ff#2=` both work), a configurable
/// delimiter, and a live preview so you can see an expansion as you type.
/// Photo Mechanic hides this in external tab files; here it's editable inline.
class CodeTableDialog extends StatefulWidget {
  /// Creates the editor over an [initial] table.
  const CodeTableDialog({required this.initial, super.key});

  /// The table to seed the form from.
  final CodeReplacements initial;

  @override
  State<CodeTableDialog> createState() => _CodeTableDialogState();
}

class _CodeTableDialogState extends State<CodeTableDialog> {
  late final TextEditingController _delimiter = TextEditingController(
    text: widget.initial.delimiter,
  );
  late final List<({TextEditingController code, TextEditingController repl})>
  _rows = [
    for (final entry in widget.initial.codes.entries)
      (
        code: TextEditingController(text: entry.key),
        repl: TextEditingController(text: _joinAlternates(entry.value)),
      ),
  ];
  late final TextEditingController _preview = TextEditingController(
    text: widget.initial.codes.isEmpty
        ? ''
        : '${widget.initial.delimiter}'
              '${widget.initial.codes.keys.first}'
              '${widget.initial.delimiter}',
  );

  @override
  void initState() {
    super.initState();
    if (_rows.isEmpty) _addRow();
  }

  @override
  void dispose() {
    _delimiter.dispose();
    _preview.dispose();
    for (final row in _rows) {
      row.code.dispose();
      row.repl.dispose();
    }
    super.dispose();
  }

  void _addRow() => setState(
    () => _rows.add((
      code: TextEditingController(),
      repl: TextEditingController(),
    )),
  );

  void _removeRow(int index) {
    setState(() {
      _rows[index].code.dispose();
      _rows[index].repl.dispose();
      _rows.removeAt(index);
    });
  }

  CodeReplacements _build() {
    final delimiter = _delimiter.text.isEmpty ? '=' : _delimiter.text;
    final codes = <String, List<String>>{};
    for (final row in _rows) {
      final code = row.code.text.trim();
      final repl = _splitAlternates(row.repl.text);
      if (code.isNotEmpty && repl.isNotEmpty) codes[code] = repl;
    }
    return CodeReplacements(delimiter: delimiter, codes: codes);
  }

  @override
  Widget build(BuildContext context) {
    final preview = expandCodes(_preview.text, _build());
    return AlertDialog(
      backgroundColor: AppColors.surfaceElevated,
      title: const Text('代码替换'),
      content: SizedBox(
        width: 520,
        child: SingleChildScrollView(
          child: Column(
            mainAxisSize: MainAxisSize.min,
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              const Text(
                '在任意模板字段的分隔符之间输入代码（如 =ff=）即展开为其文本。用“ | ”分隔候选——=ff#2= 选择第二个。',
                style: TextStyle(color: AppColors.textSecondary, fontSize: 12),
              ),
              const SizedBox(height: AppSpacing.md),
              Row(
                children: [
                  const Text(
                    '分隔符',
                    style: TextStyle(
                      color: AppColors.textSecondary,
                      fontSize: 12,
                    ),
                  ),
                  const SizedBox(width: AppSpacing.sm),
                  SizedBox(
                    width: 56,
                    child: TextField(
                      controller: _delimiter,
                      textAlign: TextAlign.center,
                      maxLength: 1,
                      style: const TextStyle(fontSize: 13),
                      onChanged: (_) => setState(() {}),
                      decoration: const InputDecoration(
                        isDense: true,
                        counterText: '',
                        border: OutlineInputBorder(),
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: AppSpacing.md),
              const DialogSection('Codes'),
              for (var i = 0; i < _rows.length; i++) _row(i),
              Align(
                alignment: Alignment.centerLeft,
                child: TextButton.icon(
                  onPressed: _addRow,
                  icon: const Icon(Icons.add, size: 16),
                  label: const Text('添加代码'),
                ),
              ),
              const SizedBox(height: AppSpacing.md),
              const DialogSection('预览'),
              TextField(
                controller: _preview,
                style: const TextStyle(fontSize: 13),
                onChanged: (_) => setState(() {}),
                decoration: const InputDecoration(
                  isDense: true,
                  hintText: '输入含 =code= 的文本以预览…',
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: AppSpacing.sm),
              Text(
                preview.isEmpty ? '—' : preview,
                style: const TextStyle(
                  color: AppColors.textPrimary,
                  fontSize: 13,
                ),
              ),
            ],
          ),
        ),
      ),
      actions: [
        TextButton(
          onPressed: () => Navigator.of(context).pop(),
          child: const Text('取消'),
        ),
        FilledButton(
          onPressed: () => Navigator.of(context).pop(_build()),
          child: const Text('Save'),
        ),
      ],
    );
  }

  Widget _row(int index) => Padding(
    padding: const EdgeInsets.only(bottom: AppSpacing.xs),
    child: Row(
      children: [
        SizedBox(
          width: 120,
          child: TextField(
            controller: _rows[index].code,
            style: const TextStyle(fontSize: 13),
            onChanged: (_) => setState(() {}),
            decoration: const InputDecoration(
              isDense: true,
              hintText: 'code',
              border: OutlineInputBorder(),
            ),
          ),
        ),
        const SizedBox(width: AppSpacing.sm),
        Expanded(
          child: TextField(
            controller: _rows[index].repl,
            style: const TextStyle(fontSize: 13),
            onChanged: (_) => setState(() {}),
            decoration: const InputDecoration(
              isDense: true,
              hintText: '替换内容（候选1 | 候选2）',
              border: OutlineInputBorder(),
            ),
          ),
        ),
        IconButton(
          iconSize: 16,
          visualDensity: VisualDensity.compact,
          tooltip: '移除',
          icon: const Icon(Icons.close_rounded),
          onPressed: () => _removeRow(index),
        ),
      ],
    ),
  );
}
