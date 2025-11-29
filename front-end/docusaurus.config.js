// @ts-check

import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'Robotics Book',
  tagline: 'Physical AI, ROS2, Digital Twin, and Humanoid Robotics',
  favicon: 'img/favicon.ico',

  future: {
    v4: true,
  },

  url: 'https://amnamahmoodobs.github.io',
  baseUrl: '/robotics-book/',

  organizationName: 'amnaMahmoodObs',
  projectName: 'robotics-book',

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          sidebarPath: './sidebars.js',
          editUrl:
            'https://github.com/amnaMahmoodObs/robotics-book/tree/main/front-end',
        },
        blog: {
          showReadingTime: true,
          feedOptions: {
            type: ['rss', 'atom'],
            xslt: true,
          },
          editUrl:
            'https://github.com/amnaMahmoodObs/robotics-book/tree/main/front-end',
        },
        theme: {
          customCss: './src/css/custom.css',
        },
      },
    ],
  ],

  themeConfig: {
    image: 'img/docusaurus-social-card.jpg',
    colorMode: {
      respectPrefersColorScheme: true,
    },
    navbar: {
      title: 'Robotics Book',
      logo: {
        alt: 'Book Logo',
        src: 'img/logo.svg',
      },
      items: [
        {
          type: 'doc',
          docId: 'chapter-1-introduction',
          position: 'left',
          label: 'Chapter 1: Introduction',
        },
        {
          type: 'doc',
          docId: 'chapter-2-ros2',
          position: 'left',
          label: 'Chapter 2: ROS 2',
        },
        {
          type: 'doc',
          docId: 'chapter-3-digital-twin',
          position: 'left',
          label: 'Chapter 3: Digital Twin',
        },
        {to: '/blog', label: 'Blog', position: 'left'},
        {
          href: 'https://github.com/amnaMahmoodObs/robotics-book',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Chapter 1',
              to: '/docs/chapter-1-introduction',
            },
            {
              label: 'Chapter 2',
              to: '/docs/chapter-2-ros2',
            },
            {
              label: 'Chapter 3',
              to: '/docs/chapter-3-digital-twin',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Stack Overflow',
              href: 'https://stackoverflow.com/questions/tagged/docusaurus',
            },
            {
              label: 'Discord',
              href: 'https://discordapp.com/invite/docusaurus',
            },
            {
              label: 'X',
              href: 'https://x.com/docusaurus',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {label: 'Blog', to: '/blog'},
            {
              label: 'GitHub Repo',
              href: 'https://github.com/amnaMahmoodObs/robotics-book',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Robotics Book`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  },
};

export default config;
