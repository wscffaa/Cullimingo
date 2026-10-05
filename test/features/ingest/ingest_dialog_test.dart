import 'package:cullimingo/features/ingest/presentation/ingest_dialog.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  testWidgets('renders the card layout, preset, and footer guidance', (
    tester,
  ) async {
    // A non-existent search root → no volumes and no auto-selected source, and
    // only synchronous existsSync I/O (safe under the widget tester's clock).
    await tester.pumpWidget(
      const ProviderScope(
        child: MaterialApp(
          home: Scaffold(
            body: IngestDialog(volumeSearchRoots: ['/cm-no-root']),
          ),
        ),
      ),
    );
    await tester.pump(); // volume scan (sync) settles

    expect(find.text('导入照片'), findsOneWidget);
    // The three cards of the what → where → named-how flow.
    expect(find.text('来源'), findsOneWidget);
    expect(find.text('目标位置'), findsOneWidget);
    expect(find.text('命名'), findsOneWidget);
    // The default naming preset is selected in the builder's dropdown.
    expect(find.text('年份 / 日期_拍摄 / 名称'), findsWidgets);
    // With no source, the source card says what to do next…
    expect(find.text('选择要扫描的存储卡或文件夹。'), findsOneWidget);
    // …and the footer explains why Import is greyed out.
    expect(find.text('请在上方选择来源'), findsOneWidget);

    // The default preset uses the Job-name element, so its row is visible.
    expect(find.text('任务名称'), findsOneWidget);
    // The pattern editor is collapsed behind the disclosure by default.
    expect(find.text('自定义文件名与文件夹'), findsOneWidget);
    expect(find.text('文件名'), findsNothing);

    // With no source/destination chosen, the Import action is disabled.
    final importButton = tester.widget<FilledButton>(
      find.widgetWithText(FilledButton, '导入'),
    );
    expect(importButton.onPressed, isNull);
  });
}
