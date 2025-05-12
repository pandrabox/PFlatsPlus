// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'PandraBox/FlatsPlus',
  tagline: 'FlatsPlusはフラット族に「可愛い、便利」を追加するアセットです',
  favicon: 'img/favicon.ico',

  // ここに本番サイトのURLを設定してください
  url: 'https://pandrabox.github.io', // ← あなたのGitHub PagesのURL
  // サイトが提供される /<baseUrl>/ パス名を設定してください
  // GitHub Pagesでのデプロイの場合、多くは '/<projectName>/' です
  baseUrl: '/pandoc/', // ← あなたのリポジトリ名

  // GitHub Pagesデプロイ用の設定
  // GitHub Pagesを使わない場合は不要です
  organizationName: 'pandrabox', // ← あなたのGitHubユーザー名
  projectName: 'pandoc', // ← あなたのリポジトリ名

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'ja',
    locales: ['ja'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // ここをあなたのリポジトリに変更してください
          // "このページを編集"リンクを削除するにはこの行を削除してください
          editUrl:
            'https://github.com/pandrabox/pandoc/tree/main/',
          routeBasePath: '/', // docsをルートパスに設定
        },
        blog: false, // blog機能を無効化
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'light',
        disableSwitch: false,
        respectPrefersColorScheme: true,
      },
      image: 'img/SocialCard.jpg',
      navbar: {
        title: 'PandraBox/FlatsPlus',
        logo: {
          alt: 'PandraBox/FlatsPlusのロゴ',
          src: 'img/FlatsPlus.png',
        },
        items: [
          {
            href: 'https://github.com/pandrabox/pandoc',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'リンク',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/pandrabox/pandoc',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} PandraBox/FlatsPlus. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;