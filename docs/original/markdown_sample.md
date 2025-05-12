---
title: Docusaurus Markdown記法サンプル
sidebar_position: 1
---

# Docusaurusで使えるMarkdown記法一覧

## 見出し
# H1
## H2
### H3

## 強調
*イタリック*  
**ボールド**  
~~打ち消し~~

## 箇条書き
- リスト1
- リスト2
  - ネスト1
  - ネスト2

1. 番号付きリスト
2. 番号付きリスト2

## コードブロック
```js
console.log('Hello!');
```

## インラインコード
`const x = 1;`

## リンク
[Google](https://www.google.com)

## 画像
![サンプル画像](../../static/img/FlatsPlus.png)

## テーブル
| 見出し1 | 見出し2 |
| ------- | ------- |
| 内容A   | 内容B   |

## 引用
> これは引用です

## チェックボックス
- [x] 完了
- [ ] 未完了

## 警告・注意・ヒント（Docusaurus拡張）
:::tip
これはヒントです
:::

:::warning
これは警告です
:::

:::info
これは情報です
:::

:::danger
これは危険です
:::
