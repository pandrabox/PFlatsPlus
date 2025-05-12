# Copilot用 ForCopilotフォルダの使い方・ルール

## 基本ルール
- ForCopilotフォルダは、Copilotが作業・記録・自動化のために自由に使う専用フォルダです
- このフォルダには「Copilotが覚えておくべきこと」や「Copilot専用のスクリプト・メモ」を保存します
- Copilotはこのメモを自由に読んだり、追記・編集したりできます
- 全ての処理はUTF-8を基準として行います（文字化け発生時は原因を調査し適宜対応）
- ForCopilotフォルダ内はCopilot専用であり、他の用途のファイルは入れません

## ファイル管理
- 重要な情報はこのREADME_CopilotMemo.txtに記録してください
- テスト用・一時的なファイルはForCopilot/tmpフォルダ以下に作成・管理します
- 「tmpをクリア」という指示があった場合は、特別な理由がない限りtmpフォルダ内のファイルを全て削除します（README_tmp.txtも含む）

## Git操作
- pushを要求された場合は、ForCopilot内のpush用ps1（copilot-push.ps1）を使ってGitHubへpushします
- push用ps1は、コミットメッセージを引数で受け取り、確認なしですぐにpushします
- 文字化け対策として、copilot-push.ps1スクリプトではUTF-8エンコーディングを設定しています

## PowerShell関連
- PowerShell（ps1）コマンド実行時は、&&（コマンド連結）が使えません
- 複数コマンドを実行したい場合は、一時的なps1ファイルをForCopilotに作成して実行してください
- PowerShellスクリプト実行時に「このシステムではスクリプトの実行が無効になっている」エラーが出る場合の対処法：
  1. 現在の実行ポリシーを確認: `Get-ExecutionPolicy`
  2. ポリシーをBypassに設定: `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force`
  3. スクリプトを実行
- スクリプト実行ポリシーの変更は積極的に行うことを強く推奨します

## Python環境
- この環境にはPythonインタプリタ（バージョン: 3.13.3）がインストールされています
- VS Codeの拡張機能と組み合わせて、CopilotはPythonスクリプトの作成・編集・実行が可能です

### PowerShellからPythonの出力を取得する方法
- 基本: `python スクリプト名.py` で実行すると標準出力がコンソールに表示されます
- 出力が表示されない場合の対処法：
  1. flushオプションを使用: `print("メッセージ", flush=True)`
  2. sysモジュールで明示的にフラッシュ:
     ```python
     import sys
     sys.stdout.write("メッセージ\n")
     sys.stdout.flush()
     ```
  3. ファイルへリダイレクト:
     ```powershell
     python スクリプト名.py > 出力ファイル.txt
     Get-Content 出力ファイル.txt
     ```