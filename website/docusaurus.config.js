// @ts-check
import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'AWS Restart Labs',
  tagline: 'Notas de laboratorio — Bootcamp AWS Restart',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://restart-labs.devera.cloud',
  baseUrl: '/',

  onBrokenLinks: 'warn',
  markdown: {
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  i18n: {
    defaultLocale: 'es',
    locales: ['es'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          path: '../LABS',
          routeBasePath: '/',
          sidebarPath: './sidebars.js',
          editUrl: undefined,
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        defaultMode: 'dark',
        disableSwitch: false,
        respectPrefersColorScheme: false,
      },
      navbar: {
        title: 'AWS Restart Labs',
        logo: {
          alt: 'AWS Restart Labs',
          src: 'img/logo.svg',
        },
        style: 'dark',
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'labsSidebar',
            position: 'left',
            label: 'Laboratorios',
          },
          {
            href: 'https://github.com/Verastian',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        copyright: `© ${new Date().getFullYear()} Verastian · AWS Restart Bootcamp`,
      },
      prism: {
        theme: prismThemes.oneDark,
        darkTheme: prismThemes.oneDark,
        additionalLanguages: ['bash', 'json', 'yaml'],
      },
      docs: {
        sidebar: {
          hideable: true,
          autoCollapseCategories: true,
        },
      },
    }),
};

export default config;
