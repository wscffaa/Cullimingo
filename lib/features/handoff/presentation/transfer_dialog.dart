import 'dart:async';

import 'package:cullimingo/app/theme/tokens.dart';
import 'package:cullimingo/core/files/destination_check.dart';
import 'package:cullimingo/core/files/directory_picker.dart';
import 'package:cullimingo/core/settings/app_settings.dart';
import 'package:cullimingo/features/handoff/data/transfer_service.dart';
import 'package:cullimingo/shared/widgets/dialog_kit.dart';
import 'package:flutter/material.dart';
import 'package:path/path.dart' as p;

/// A confirmed copy/move, returned by [showTransferDialog]. The plan is built
/// and run non-modally by the caller so the grid stays scrollable during the
/// transfer.
class TransferRequest {
  /// Creates a request.
  const TransferRequest({
    required this.sources,
    required this.destinationRoot,
    required this.mode,
    required this.includeSidecars,
    required this.openWhenDone,
  });

  /// Absolute source photo paths to transfer.
  final List<String> sources;

  /// Destination root, including the optional subfolder.
  final String destinationRoot;

  /// Whether to copy or move.
  final TransferMode mode;

  /// Whether to carry each photo's `.xmp` sidecar along.
  final bool includeSidecars;

  /// Whether to open the destination folder once the run finishes.
  final bool openWhenDone;
}

/// Shows the copy/move dialog for [sources] (the current selection or focused
/// photo). Returns the confirmed [TransferRequest], or null if cancelled.
Future<TransferRequest?> showTransferDialog(
  BuildContext context, {
  required List<String> sources,
  required TransferMode mode,
}) {
  return showDialog<TransferRequest>(
    context: context,
    builder: (_) => _TransferDialog(sources: sources, mode: mode),
  );
}

class _TransferDialog extends StatefulWidget {
  const _TransferDialog({required this.sources, required this.mode});

  final List<String> sources;
  final TransferMode mode;

  @override
  State<_TransferDialog> createState() => _TransferDialogState();
}

class _TransferDialogState extends State<_TransferDialog> {
  String? _destination;
  bool _includeSidecars = true;
  bool _openWhenDone = false;
  final TextEditingController _subfolder = TextEditingController();

  bool get _isMove => widget.mode == TransferMode.move;

  @override
  void initState() {
    super.initState();
    unawaited(
      AppSettings.load().then((s) {
        if (mounted) setState(() => _destination = s.lastDestination);
      }),
    );
  }

  @override
  void dispose() {
    _subfolder.dispose();
    super.dispose();
  }

  /// The destination root, including the optional subfolder.
  String? _resolvedDestination() {
    final dest = _destination;
    if (dest == null) return null;
    final sub = _subfolder.text.trim();
    return sub.isEmpty ? dest : p.join(dest, sub);
  }

  Future<void> _pickDestination() async {
    final dir = await pickDirectory(initialDirectory: _destination);
    if (dir != null && mounted) {
      setState(() => _destination = dir);
      // So a later run can tell when this folder's drive is gone.
      unawaited(rememberDestinationVolume(dir));
    }
  }

  void _submit() {
    final root = _resolvedDestination();
    if (root == null) return;
    unawaited(
      updateSettings((s) => s.setLastDestination(_destination!)),
    );
    Navigator.of(context).pop(
      TransferRequest(
        sources: widget.sources,
        destinationRoot: root,
        mode: widget.mode,
        includeSidecars: _includeSidecars,
        openWhenDone: _openWhenDone,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final count = widget.sources.length;
    final verb = _isMove ? '移动' : '复制';
    return AlertDialog(
      title: Text('$verb $count 张照片'),
      content: SizedBox(
        width: 460,
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            const DialogSection('目标位置'),
            DialogPathRow(
              path: _destination,
              onPick: _pickDestination,
              hint: '选择文件夹…',
            ),
            const SizedBox(height: AppSpacing.sm),
            TextField(
              controller: _subfolder,
              decoration: dialogInputDecoration(
                '子文件夹（可选，如 selects）',
              ),
              style: const TextStyle(
                color: AppColors.textPrimary,
                fontSize: 14,
              ),
            ),
            const SizedBox(height: AppSpacing.md),
            DialogCheckbox(
              value: _includeSidecars,
              onChanged: (v) => setState(() => _includeSidecars = v ?? true),
              label: '包含 XMP 附属文件',
            ),
            DialogCheckbox(
              value: _openWhenDone,
              onChanged: (v) => setState(() => _openWhenDone = v ?? false),
              label: '完成后打开文件夹',
            ),
            const SizedBox(height: AppSpacing.md),
            Text(
              _isMove
                  ? '移动会把原文件复制到目标位置，并在每次复制校验通过后才将其从当前文件夹移除。'
                  : '复制会生成原文件的副本；原文件保留在原处。',
              style: const TextStyle(
                color: AppColors.textSecondary,
                fontSize: 11,
              ),
            ),
          ],
        ),
      ),
      actions: [
        TextButton(
          onPressed: () => Navigator.of(context).pop(),
          child: const Text('取消'),
        ),
        FilledButton(
          onPressed: _destination == null ? null : _submit,
          child: Text('$verb ${widget.sources.length} 张'),
        ),
      ],
    );
  }
}
