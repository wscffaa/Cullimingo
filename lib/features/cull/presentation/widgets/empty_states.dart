import 'package:cullimingo/app/theme/tokens.dart';
import 'package:cullimingo/core/version/app_version.g.dart';
import 'package:cullimingo/features/filter/presentation/filter_providers.dart';
import 'package:flutter/material.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';

/// The first-launch empty grid: branding lockup + an "open folder" call to
/// action.
class CullEmptyState extends StatelessWidget {
  /// Creates the empty state.
  const CullEmptyState({required this.onOpenFolder, super.key});

  /// Called to open a folder.
  final Future<void> Function() onOpenFolder;

  @override
  Widget build(BuildContext context) {
    // Autofocus so app-level shortcuts (⌘O) work on first launch, when no grid
    // exists to hold focus.
    return Focus(
      autofocus: true,
      child: Center(
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            // Logo lockup: the flamingo mark over the wordmark.
            Image.asset(
              'assets/branding/cullimingo_mark.png',
              height: 96,
              filterQuality: FilterQuality.high,
            ),
            const SizedBox(height: AppSpacing.lg),
            const Text(
              'Cullimingo',
              style: TextStyle(
                color: AppColors.textPrimary,
                fontSize: 30,
                fontWeight: FontWeight.w600,
                letterSpacing: 1.5,
              ),
            ),
            const SizedBox(height: AppSpacing.sm),
            const Text(
              '打开 RAW 或 JPEG 文件夹开始筛选',
              style: TextStyle(color: AppColors.textSecondary),
            ),
            const SizedBox(height: AppSpacing.lg),
            FilledButton.icon(
              onPressed: onOpenFolder,
              icon: const Icon(Icons.folder_open, size: 18),
              label: const Text('打开文件夹'),
            ),
            const SizedBox(height: AppSpacing.lg),
            const Text(
              '版本 $kAppVersion',
              style: TextStyle(
                color: AppColors.textSecondary,
                fontSize: 11,
              ),
            ),
          ],
        ),
      ),
    );
  }
}

/// Shown when a filter is active but nothing matches: offers to clear filters.
class NoMatchesState extends ConsumerWidget {
  /// Creates the no-matches state.
  const NoMatchesState({super.key});

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.min,
        children: [
          const Icon(
            Icons.filter_alt_off_outlined,
            size: 40,
            color: AppColors.textSecondary,
          ),
          const SizedBox(height: AppSpacing.md),
          const Text(
            '没有符合当前筛选的照片',
            style: TextStyle(color: AppColors.textSecondary),
          ),
          const SizedBox(height: AppSpacing.lg),
          TextButton.icon(
            onPressed: () =>
                ref.read(photoFilterControllerProvider.notifier).clear(),
            icon: const Icon(Icons.clear_all, size: 18),
            label: const Text('清除筛选'),
          ),
        ],
      ),
    );
  }
}
