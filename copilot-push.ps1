# GitHubへの変更をプッシュする簡易スクリプト（Copilot Agent用）
# PowerShellで実行するスクリプト - 確認なしですぐにプッシュします

param (
    [Parameter(Mandatory=$true)]
    [string]$CommitMessage = "Copilot Agentによる自動更新"
)

# カレントディレクトリをDocusaurusプロジェクトに設定
$projectPath = Split-Path -Parent $MyInvocation.MyCommand.Path
Set-Location -Path $projectPath

# 変更をステージング
Write-Host "変更をステージングしています..." -ForegroundColor Cyan
git add .

# コミット
Write-Host "変更をコミットしています..." -ForegroundColor Cyan
git commit -m $CommitMessage

# GitHubにプッシュ
Write-Host "GitHubにプッシュしています..." -ForegroundColor Cyan
git push

# 完了メッセージ
Write-Host "処理が完了しました！" -ForegroundColor Green
Write-Host "コミットメッセージ: $CommitMessage" -ForegroundColor Green
