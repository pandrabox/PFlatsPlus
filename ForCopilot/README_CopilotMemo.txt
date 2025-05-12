Copilot用 ForCopilotフォルダの使い方・ルール

- ForCopilotフォルダは、Copilotが作業・記録・自動化のために自由に使う専用フォルダです。
- このフォルダには「Copilotが覚えておくべきこと」や「Copilot専用のスクリプト・メモ」などを入れます。
- Copilotはこのメモを自由に読んだり、追記・編集したりできます。
- PowerShell（ps1）コマンド実行時は、&&（コマンド連結）が使えません。複数コマンドを実行したい場合は、一時的なps1ファイルをForCopilotに作成して実行してください。
- pushを要求された場合は、ForCopilot内のpush用ps1（copilot-push.ps1）を使ってGitHubへpushします。
- push用ps1は、コミットメッセージを引数で受け取り、確認なしですぐにpushします。
- ForCopilotフォルダ内はCopilot専用です。他の用途のファイルは入れません。
- 必要に応じて、このメモに追記・修正してください。
