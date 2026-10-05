import 'package:cullimingo/app/theme/tokens.dart';
import 'package:flutter/material.dart';

/// Confirms moving the folder's [count] rejected photos to the OS trash.
/// Resolves to `true` on confirm, `false`/`null` on cancel.
Future<bool?> showDeleteRejectsDialog(
  BuildContext context, {
  required int count,
}) => _showTrashConfirmDialog(
  context,
  title: '删除已剔除照片',
  count: count,
  descriptor: count == 1 ? '已剔除照片' : '已剔除照片',
);

/// Confirms moving [count] selected photos to the OS trash (the right-click
/// context menu's "Delete…" entry). Resolves to `true` on confirm,
/// `false`/`null` on cancel.
Future<bool?> showDeleteSelectedPhotosDialog(
  BuildContext context, {
  required int count,
}) => _showTrashConfirmDialog(
  context,
  title: count == 1 ? '删除照片' : '删除 $count 张照片',
  count: count,
  descriptor: '张照片',
);

Future<bool?> _showTrashConfirmDialog(
  BuildContext context, {
  required String title,
  required int count,
  required String descriptor,
}) {
  return showDialog<bool>(
    context: context,
    builder: (context) => AlertDialog(
      title: Text(title),
      content: Text(
        '将 $count $descriptor移到废纸篓？\n\n原图及其 .xmp 附属文件将离开此文件夹。不会永久删除——可从废纸篓恢复。',
      ),
      actions: [
        TextButton(
          onPressed: () => Navigator.of(context).pop(false),
          child: const Text('取消'),
        ),
        TextButton(
          style: TextButton.styleFrom(foregroundColor: AppColors.labelRed),
          onPressed: () => Navigator.of(context).pop(true),
          child: const Text('移到废纸篓'),
        ),
      ],
    ),
  );
}
