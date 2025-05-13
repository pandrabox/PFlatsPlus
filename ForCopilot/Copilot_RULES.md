# Copilot専用運用仕様書（Copilot_RULES.md）

## プロジェクトの目的・運用方針
- original.md だけを編集・管理すれば、分割・構造化・公開まで全自動で完結するDocusaurusドキュメント自動化プロジェクト。
- original.md を編集し、md_divider.py を実行するだけで、
  - original.md をH1ごとに自動分割
  - Docusaurus用frontmatter（title, slug, sidebar_positionなど）を自動付与
  - docs/divided/配下に最適な構造で出力
  - sidebars.jsも自動生成
  - 001.md（概要）が常にトップページ（/）として公開される
- そのままGitHub Pagesで静的サイトとして即公開できる
- 「最小の手間で、常に最新・最適なドキュメントサイトを維持できる」ワークフローを実現


## ビルドを実行　命令の定義
- Copilotは「ビルドを実行」という命令を受けたら次を行います
  - この文書(Copilot_RULES.md)を再確認する
  - 翻訳に関する文書(TranslationInstructions.md)を確認する
  - ローカライズを実行する(i18nフォルダへ)
  - 日本語を作成する(docsフォルダへ)
  - pushをする


## Divideを実行 命令の定義
- Copilotは「Divideを実行」という命令を受けたら次を行います
  - この文書(Copilot_RULES.md)を再確認する
  - md_dividerを使ってdocs/original.mdからdocs/dividedへの分割を実行する
  - pushはしません

---

## 運用上の注意・推奨事項
- 人間が作業するのは基本的に docs/original.md のみ
- docs フォルダには original.md と自動生成される divided フォルダのみが存在すべき（他のファイルやフォルダは原則禁止）
- 環境によって res というフォルダが作成されることがあるが、これは好ましくなくバグの原因となるため注意
- 画像は全て static/img 配下に保存すること（docs/ や divided/ には画像を置かない）

---

## ForCopilotフォルダの基本ルール
- Copilotが作業・記録・自動化のために自由に使う専用フォルダ
- 「Copilotが覚えておくべきこと」や「Copilot専用のスクリプト・メモ」を保存
- 全ての処理はUTF-8を基準
- 他の用途のファイルは入れない

## ファイル管理
- 重要な情報はこのCopilot_RULES.mdに記録
- テスト用・一時的なファイルはForCopilot/tmpフォルダ以下に作成・管理
- 「tmpをクリア」指示時はtmpフォルダ内のファイルを全削除

## Git操作
- push要求時はForCopilot内のcopilot-push.ps1でGitHubへpush
- コミットメッセージを引数で受け取り、確認なしでpush
- copilot-push.ps1はUTF-8エンコーディングを設定

## PowerShell関連
- PowerShell（ps1）コマンド実行時は、&&（コマンド連結）が使えない
- 複数コマンドは一時ps1ファイルを作成して実行
- スクリプト実行が無効な場合：
  1. `Get-ExecutionPolicy` で確認
  2. `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force` でBypass
  3. スクリプトを実行
- スクリプト実行ポリシーの変更は積極的に推奨

## Python環境
- Pythonインタプリタ（3.13.3）がインストール済み
- VS Code拡張機能と組み合わせてPythonスクリプトの作成・実行が可能

### PowerShellからPythonの出力を取得する方法
- 基本: `python スクリプト名.py` で標準出力が表示される
- 出力が表示されない場合：
  1. flushオプション: `print("メッセージ", flush=True)`
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

## md_divider.py・md_divider_readme.mdについて
- ForCopilot/md_divider/ にMarkdown分割用ツール（md_divider.py）とその説明（md_divider_readme.md）を設置
- md_divider.pyは大きなMarkdownファイルをH1見出しごとに分割し、Docusaurus用frontmatter（title, slug, sidebar_positionなど）を自動付与
- H1見出しに「@フォルダ名@タイトル」形式を使うと、指定フォルダに分割ファイルを出力
- 001.md（概要）は常にslug: / となりトップページになる

---
