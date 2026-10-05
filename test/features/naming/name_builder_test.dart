import 'package:cullimingo/features/naming/domain/name_preset.dart';
import 'package:cullimingo/features/naming/presentation/name_builder.dart';
import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  Widget host({
    required NamePreset initial,
    required ValueChanged<NamePreset> onChanged,
    List<NamePreset> saved = const [],
    ValueChanged<NamePreset>? onSave,
    ValueChanged<String>? onDelete,
  }) => MaterialApp(
    home: Scaffold(
      body: SingleChildScrollView(
        child: NameBuilder(
          initial: initial,
          savedPresets: saved,
          onChanged: onChanged,
          onSavePreset: onSave ?? (_) {},
          onDeletePreset: onDelete ?? (_) {},
        ),
      ),
    ),
  );

  const empty = NamePreset(name: '', folderPattern: '', filePattern: '');

  testWidgets('clicking a plain element inserts its token into the filename', (
    tester,
  ) async {
    NamePreset? emitted;
    await tester.pumpWidget(
      host(initial: empty, onChanged: (p) => emitted = p),
    );

    await tester.tap(find.text('原始文件名'));
    await tester
        .pump(); // insert focuses the field; don't settle (cursor blink)

    expect(emitted?.filePattern, '{origname}');
  });

  testWidgets('elements insert at the caret, one after another', (
    tester,
  ) async {
    NamePreset? emitted;
    await tester.pumpWidget(
      host(initial: empty, onChanged: (p) => emitted = p),
    );

    await tester.tap(find.text('原始文件名'));
    await tester.pump();
    await tester.tap(find.text('相机'));
    await tester.pump();

    expect(emitted?.filePattern, '{origname}{camera}');
  });

  testWidgets('the counter element inserts a seq token with chosen digits', (
    tester,
  ) async {
    NamePreset? emitted;
    await tester.pumpWidget(
      host(initial: empty, onChanged: (p) => emitted = p),
    );

    await tester.tap(find.text('计数器 ▾'));
    await tester.pumpAndSettle(); // menu opens (no field focus yet)
    await tester.tap(find.text('4 位').last);
    await tester.pump();

    expect(emitted?.filePattern, '{seq:4}');
  });

  testWidgets('the date element inserts a date token in the chosen format', (
    tester,
  ) async {
    NamePreset? emitted;
    await tester.pumpWidget(
      host(initial: empty, onChanged: (p) => emitted = p),
    );

    await tester.tap(find.text('日期 / 时间 ▾'));
    await tester.pumpAndSettle();
    await tester.tap(find.text('年份（2026）').last);
    await tester.pump();

    expect(emitted?.filePattern, '{date:year}');
  });

  testWidgets('editing a field emits the new pattern', (tester) async {
    NamePreset? emitted;
    await tester.pumpWidget(
      host(
        initial: const NamePreset(
          name: '',
          folderPattern: '',
          filePattern: '{origname}',
        ),
        onChanged: (p) => emitted = p,
      ),
    );

    // `{origname}` matches the Keep-filenames preset, so the editor starts
    // collapsed — open it first.
    await tester.tap(find.textContaining('自定义'));
    await tester.pump();

    // The first TextField is the filename field; typing replaces its content.
    await tester.enterText(find.byType(TextField).first, '{origname}_v2');
    await tester.pump();

    expect(emitted?.filePattern, '{origname}_v2');
  });

  testWidgets('a preset scheme starts collapsed; the disclosure opens it', (
    tester,
  ) async {
    await tester.pumpWidget(
      host(initial: NamePreset.builtIns.first, onChanged: (_) {}),
    );

    // A known preset needs no pattern editing — the editor is folded away.
    expect(find.text('文件名'), findsNothing);
    expect(find.text('元素'), findsNothing);

    await tester.tap(find.text('自定义文件名与文件夹'));
    await tester.pump();

    expect(find.text('文件名'), findsOneWidget);
    expect(find.text('元素'), findsOneWidget);
  });

  testWidgets('a custom scheme starts with the pattern editor open', (
    tester,
  ) async {
    await tester.pumpWidget(host(initial: empty, onChanged: (_) {}));

    expect(find.text('文件名'), findsOneWidget);
    expect(find.text('元素'), findsOneWidget);
  });

  testWidgets('selecting a preset loads its scheme and shows the example', (
    tester,
  ) async {
    NamePreset? emitted;
    await tester.pumpWidget(
      host(initial: NamePreset.builtIns.first, onChanged: (p) => emitted = p),
    );

    await tester.tap(find.byType(DropdownButton<String>));
    await tester.pumpAndSettle();
    await tester.tap(find.text('时间戳').last);
    await tester.pumpAndSettle();

    expect(emitted?.name, '时间戳');
    expect(emitted!.filePattern, contains('{seq:4}'));
    // The example is rendered from the engine with the sample data.
    expect(find.textContaining('2026-07-02_143005'), findsOneWidget);
  });
}
