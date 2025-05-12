# GitHubへの変更をプッシュするPowerShellスクリプト
param (
    [Parameter(Mandatory=$true)]
    [string]$CommitMessage
)

# カレントディレクトリをDocusaurusプロジェクトに設定
$projectPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location -Path $projectPath

# ステータスの確認
Write-Host "現在の変更状況を確認しています..." -ForegroundColor Cyan
git status

# 変更内容の確認（オプション）
Write-Host "`n変更内容を表示します..." -ForegroundColor Cyan
git diff --stat

# 確認プロンプト
$confirmation = Read-Host "`n上記の変更をコミット・プッシュしますか？[y/n]"
if ($confirmation -ne 'y') {
    Write-Host "処理を中断しました。" -ForegroundColor Yellow
    exit
}

# 変更をステージング
Write-Host "`n変更をステージングしています..." -ForegroundColor Cyan
git add .

# コミット
Write-Host "`n変更をコミットしています..." -ForegroundColor Cyan
git commit -m $CommitMessage

# GitHubにプッシュ
Write-Host "`nGitHubにプッシュしています..." -ForegroundColor Cyan
git push

# 完了メッセージ
Write-Host "`n処理が完了しました！" -ForegroundColor Green
Write-Host "コミットメッセージ: $CommitMessage" -ForegroundColor Green
Write-Host "GitHub Actionsが自動的にデプロイを開始します。数分後に反映されるでしょう。" -ForegroundColor Green
