# Markdown Divider (マークダウン分割ツール)

このPythonスクリプトは、大きなMarkdownファイルを複数の小さなファイルに分割し、Docusaurusで使用するためのフロントマターを追加するツールです。

## 機能

- 大きなMarkdownファイルをH1見出し（# で始まる行）ごとに分割
- 各ファイルにDocusaurusのフロントマターを自動追加
- ファイル名を連番（001.md, 002.md, ...）で保存
- 特殊な書式でフォルダ分けに対応: `# @フォルダ名@タイトル`

## 使い方

```powershell
python md_divider.py <Markdownファイルパス>
```

### 例

```powershell
python c:\P\docusaurus\docusaurus\ForCopilot\md_divider.py c:\P\docusaurus\docusaurus\ForCopilot\tmp\test_document.md
```

## 入力ファイル形式

通常のMarkdownファイルを使用します。以下の形式に対応しています:

1. 通常のH1見出し（ファイル分割ポイント）
```
# 見出しタイトル
内容...
```

2. フォルダ指定付きH1見出し
```
# @フォルダ名@見出しタイトル
内容...
```

3. ネストしたフォルダ指定
```
# @親フォルダ/子フォルダ@見出しタイトル
内容...
```

## 出力形式

- 入力ファイルと同じディレクトリに「Outp」フォルダを作成
- H1見出しごとに連番のファイル（001.md, 002.md, ...）を作成
- フォルダ指定がある場合は該当フォルダ内にファイルを作成
- 各ファイルの先頭にDocusaurusのフロントマターを追加:

```markdown
---
title: 見出しタイトル
sidebar_position: (連番)
---
(元の内容)
```

## 注意点

- UTF-8エンコーディングで処理します
- 入力ファイルの最初のH1見出しの前にある内容は無視されます
- ファイル名は元のファイル名に関係なく、常に連番になります
