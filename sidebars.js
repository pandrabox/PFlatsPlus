// @ts-check

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

/**
 * Creating a sidebar enables you to:
 - create an ordered group of docs
 - render a sidebar for each doc of that group
 - provide next/previous navigation

 The sidebars can be generated from the filesystem, or explicitly defined here.

 Create as many sidebars as you want.

 @type {import('@docusaurus/plugin-content-docs').SidebarsConfig}
 */
const sidebars = {
  dividedSidebar: [
    {
      type: 'category',
      label: '簡単ガイド',
      collapsed: false,
      items: [
        'divided/簡単ガイド/001',
        'divided/簡単ガイド/002',
        'divided/簡単ガイド/003',
      ],
    },
    {
      type: 'category',
      label: '詳細ガイド',
      collapsed: false,
      items: [
        'divided/詳細ガイド/004',
      ],
    },
  ],
};

export default sidebars;
