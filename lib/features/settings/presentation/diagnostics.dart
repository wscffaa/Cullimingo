import 'dart:async';

import 'package:cullimingo/core/logging/app_logger.dart';
import 'package:cullimingo/core/version/app_version.g.dart';
import 'package:flutter/material.dart';
import 'package:talker_flutter/talker_flutter.dart';

// [kAppVersion] now lives in the generated `core/version/app_version.g.dart`
// (mirrored from pubspec.yaml by `tool/gen_version.dart`).

/// Pushes the in-app **log viewer** (`BUILD_PLAN.md` §8): a full-screen
/// [TalkerScreen] over the shared [appTalker] history, themed to match the app.
/// Lets you read/copy/share runtime diagnostics and captured errors.
void showLogViewer(BuildContext context) {
  unawaited(
    Navigator.of(context).push(
      MaterialPageRoute<void>(
        builder: (context) => TalkerScreen(
          talker: appTalker,
          appBarTitle: 'Cullimingo 日志',
          theme: TalkerScreenTheme.fromTheme(Theme.of(context)),
        ),
      ),
    ),
  );
}

/// Shows the standard **About** dialog (`BUILD_PLAN.md` §8) with the app name,
/// version and a one-line description. Its built-in "View licenses" button
/// opens the [LicensePage] listing every bundled package's open-source licence.
void showAboutCullimingo(BuildContext context) {
  showAboutDialog(
    context: context,
    applicationName: 'Cullimingo',
    applicationVersion: kAppVersion,
    applicationIcon: Image.asset(
      'assets/branding/cullimingo_icon_256.png',
      width: 64,
      height: 64,
    ),
    applicationLegalese: 'Open-source · github.com/nielsfranke/Cullimingo',
    children: const [
      SizedBox(height: 12),
      Text(
        '一款快速的跨平台照片筛选应用。导入、筛选、过滤、导出、移交——速度即产品。',
      ),
    ],
  );
}
