# GitHubへの変更をプッシュする簡易スクリプト（Copilot Agent用）
# PowerShellで実行するスクリプト - 確認なしですぐにプッシュします

# エンコーディングをUTF-8に設定（文字化け対策）
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$OutputEncoding = [System.Text.Encoding]::UTF8

param (
    [Parameter(Mandatory=$true)]
    [string]$CommitMessage = "Copilot Agentによる自動更新"
)

# カレントディレクトリをDocusaurusプロジェクトに設定
$projectPath = Split-Path -Parent (Split-Path -Parent $MyInvocation.MyCommand.Path)
Set-Location -Path $projectPath

# 変更をステージング
Write-Host "Staging changes..." -ForegroundColor Cyan
git add .

# コミット
Write-Host "Committing changes..." -ForegroundColor Cyan
git commit -m $CommitMessage

# GitHubにプッシュ
Write-Host "Pushing to GitHub..." -ForegroundColor Cyan
git push

# 完了メッセージ
Write-Host "Done!" -ForegroundColor Green
Write-Host 'Commit message: ' $CommitMessage -ForegroundColor Green
