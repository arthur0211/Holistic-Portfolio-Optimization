/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  i18n: {
    locales: ['pt-BR', 'en'],
    defaultLocale: 'pt-BR',
    // localeDetection: false, // Optional: to disable auto-detection and rely on path prefix
  },
};

module.exports = nextConfig; 