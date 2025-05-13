# 概要
この文書はCopilotに「ローカライズを実行」と指示したときの処理内容を定めます

# 実行内容

- ルートフォルダにi18nフォルダを作成する。既にあれば、中身を削除する
- 「英語」について次を実行する
  - i18n/en/docusaurus-plugin-content-docs/current フォルダを作成する
  - docs/original.md を英語に翻訳したファイルを作成し、i18n/en/docusaurus-plugin-content-docs/current/original.md に保存する
  - 下記コマンドで分割ファイルを生成し、i18n/en/docusaurus-plugin-content-docs/current/divided/ フォルダに保存する

```powershell
python ForCopilot/md_divider/md_divider.py i18n/en/docusaurus-plugin-content-docs/current/original.md i18n/en/docusaurus-plugin-content-docs/current/divided
```
