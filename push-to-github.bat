@echo off
REM GitHubへの変更をプッシュするバッチファイル
set /p commit_msg="コミットメッセージを入力してください: "

echo 現在の変更状況を確認しています...
git status

echo 変更をステージングしています...
git add .

echo 変更をコミットしています...
git commit -m "%commit_msg%"

echo GitHubにプッシュしています...
git push

echo 処理が完了しました！
echo コミットメッセージ: %commit_msg%
echo GitHub Actionsが自動的にデプロイを開始します。数分後に反映されるでしょう。

pause
