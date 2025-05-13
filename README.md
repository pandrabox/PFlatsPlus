# 概要
- [Docusaurus](https://docusaurus.io/) を自分的に使いやすくしたものです。github copilot agent使用前提で最適化しています
- 最終的にはgithubpages直下にシンプルなDocsが展開されるものができます 1Projectのドキュメントのために1リポジトリを使う構造です（サイドバーの分割がうまくいかなかったので）

# 特殊な箇所
- .vscode/setting.json … VSCodeに貼りつけた画像をstatic/imageにしまいます。本当はdivided時等にコード変換する必要があるのですが未実装です。すぐやると思います
- original.md … メインコンテンツです。全てのページ内容をここに書きます。H1相当で自動的に分割され@@で囲むことでフォルダ宣言ができます
  - 目的としては、多言語対応をするとき１ファイルにしたかったという話です
  - 開発時はhttp://localhost:3000/pandoc/originalで様子が見れます　pandocの場所はリポジトリ名
- ForCopilot … Copilotサンに実行してもらったりするフォルダ
  - copilot_RULES.md agentに守ってほしいルール。再起動時等にまず明示して読んでもらいます
  - md_divider … 実行するとoriginal.mdをdividedフォルダに分割します
  - copilot-push.ps1