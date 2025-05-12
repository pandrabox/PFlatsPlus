#!/bin/bash
# GitHubへの変更をプッシュするシェルスクリプト

# コミットメッセージの入力
echo "コミットメッセージを入力してください:"
read commit_msg

# カレントディレクトリをDocusaurusプロジェクトに設定
cd "$(dirname "$0")"

# ステータスの確認
echo -e "\e[36m現在の変更状況を確認しています...\e[0m"
git status

# 変更内容の確認（オプション）
echo -e "\n\e[36m変更内容を表示します...\e[0m"
git diff --stat

# 確認プロンプト
echo -e "\n上記の変更をコミット・プッシュしますか？[y/n]"
read confirmation
if [[ $confirmation != "y" ]]; then
    echo -e "\e[33m処理を中断しました。\e[0m"
    exit 0
fi

# 変更をステージング
echo -e "\n\e[36m変更をステージングしています...\e[0m"
git add .

# コミット
echo -e "\n\e[36m変更をコミットしています...\e[0m"
git commit -m "$commit_msg"

# GitHubにプッシュ
echo -e "\n\e[36mGitHubにプッシュしています...\e[0m"
git push

# 完了メッセージ
echo -e "\n\e[32m処理が完了しました！\e[0m"
echo -e "\e[32mコミットメッセージ: $commit_msg\e[0m"
echo -e "\e[32mGitHub Actionsが自動的にデプロイを開始します。数分後に反映されるでしょう。\e[0m"
