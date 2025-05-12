Copilot用 ForCopilotフォルダの使い方・ルール

- ForCopilotフォルダは、Copilotが作業・記録・自動化のために自由に使う専用フォルダです。
- このフォルダには「Copilotが覚えておくべきこと」や「Copilot専用のスクリプト・メモ」などを入れます。
- Copilotはこのメモを自由に読んだり、追記・編集したりできます。
- 全ての処理はUTF-8を基準として行うこととする。文字化けが発生した場合は原因を調査し、適宜対応する。
- PowerShell（ps1）コマンド実行時は、&&（コマンド連結）が使えません。複数コマンドを実行したい場合は、一時的なps1ファイルをForCopilotに作成して実行してください。
- pushを要求された場合は、ForCopilot内のpush用ps1（copilot-push.ps1）を使ってGitHubへpushします。
- push用ps1は、コミットメッセージを引数で受け取り、確認なしですぐにpushします。
- 文字化け対策として、copilot-push.ps1スクリプトではUTF-8エンコーディングを設定しています。
- ForCopilotフォルダ内はCopilot専用です。他の用途のファイルは入れません。
- テスト用・一時的なファイルはForCopilot/tmpフォルダ以下に作成・管理します。
- 「tmpをクリア」という指示があった場合は、特別な理由がない限りtmpフォルダ内のファイルを全て削除します（README_tmp.txtも含む）。
- 重要な情報はtmpフォルダ内ではなく、このREADME_CopilotMemo.txtに記録してください。
- 必要に応じて、このメモに追記・修正してください。

【Python実行環境についてのメモ】
- この環境にはPythonインタプリタ（バージョン: 3.13.3）がインストールされています。
- VS Codeの拡張機能と組み合わせて、CopilotはPythonスクリプトの作成・編集・実行が可能です。
- Python関連の参考ファイルとテスト結果は、ForCopilot/tmpフォルダに保存されています。
- 詳細なテスト結果は ForCopilot/tmp/PYTHON_OUTPUT_TEST_README.txt を参照してください。

【PowerShellからPythonの出力を取得する方法】
- 通常は単純に「python スクリプト名.py」で実行すると標準出力がコンソールに表示されます。
- 出力が表示されない場合は、以下の方法を試してください：
  1. Pythonスクリプト内で flush=True オプションを使用する：
     print("メッセージ", flush=True)
  2. sysモジュールを使って明示的にフラッシュする：
     import sys
     sys.stdout.write("メッセージ\n")
     sys.stdout.flush()
  3. ファイルへリダイレクトする：
     python スクリプト名.py > 出力ファイル.txt
     Get-Content 出力ファイル.txt
- 環境によって動作が異なる場合がありますが、上記の方法を組み合わせることで対応可能です。

【PowerShellスクリプト実行ポリシーについて】
- PowerShellスクリプト(.ps1ファイル)を実行しようとして「このシステムではスクリプトの実行が無効になっている」というエラーが出る場合があります。
- これはPowerShellの実行ポリシーの制限によるものです。
- この環境では、スクリプト実行のために積極的にセキュリティポリシーを緩めることを推奨します：
  1. 現在の実行ポリシーを確認する：
     Get-ExecutionPolicy
  2. ポリシーを最も緩い「Bypass」に設定する：
     Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
  3. スクリプトを実行する
- スクリプト実行ポリシーの変更は積極的に行うことを強く推奨します
