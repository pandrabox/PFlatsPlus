// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'PandraBox/FlatsPlus',
  tagline: 'FlatsPlusはフラット族に「可愛い、便利」を追加するアセットです',
  favicon: 'img/favicon.ico',
  trailingSlash: true, // GitHub Pages での問題を解決するため、末尾のスラッシュを明示

  // ここに本番サイトのURLを設定してください
  url: 'https://pandrabox.github.io', // ← あなたのGitHub PagesのURL
  // サイトが提供される /<baseUrl>/ パス名を設定してください
  // GitHub Pagesでのデプロイの場合、多くは '/<projectName>/' です
  baseUrl: '/pandoc/', // ← あなたのリポジトリ名

  // GitHub Pagesデプロイ用の設定
  // GitHub Pagesを使わない場合は不要です
  organizationName: 'pandrabox', // ← あなたのGitHubユーザー名
  projectName: 'pandoc', // ← あなたのリポジトリ名

  onBrokenLinks: 'warn', // エラーではなく警告として扱う
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'ja',
    locales: ['ja', 'en'],
    localeConfigs: {
      ja: { label: '日本語' },
      en: { label: 'English' }
    }
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // "このページを編集"リンクを削除
          editUrl: undefined,
          routeBasePath: '/', // docsをルートパスに設定
          // homePageId: 'pandoc', // 削除: Docusaurus v3では非対応
          // pandoc.mdをホームページとして設定するには、docs/pandoc.mdのfrontmatterにslug: '/'を追加してください
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
      docs: {
        sidebar: {
          autoCollapseCategories: false, // サイドバーを最初から全展開
        },
      },
      // footer: {
      //   style: 'dark',
      //   links: [
      //     {
      //       title: 'リンク',
      //       items: [
      //         {
      //           label: 'GitHub',
      //           href: 'https://github.com/pandrabox/pandoc',
      //         },
      //       ],
      //     },
      //   ],
      //   copyright: `Copyright © ${new Date().getFullYear()} PandraBox/FlatsPlus. Built with Docusaurus.`,
      // },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;