// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'PandraBox/FlatsPlus',
  tagline: 'FlatsPlusはフラット族に「可愛い、便利」を追加します',
  favicon: 'img/favicon.ico',
  trailingSlash: true, 

  url: 'https://pandrabox.github.io', 
  baseUrl: '/pandoc/', 
  organizationName: 'pandrabox', 
  projectName: 'pandoc', 
  onBrokenLinks: 'warn', 
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'ja',
    locales: ['ja']
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          editUrl: undefined,
          routeBasePath: '/', 
        },
        blog: false, 
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
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;