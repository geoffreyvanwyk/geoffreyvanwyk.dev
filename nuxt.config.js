import tailwindTypography from '@tailwindcss/typography'
const tailwindHeroPatterns = require('tailwindcss-hero-patterns')

export default {
  // Target: https://go.nuxtjs.dev/config-target
  target: 'static',

  // Global page headers: https://go.nuxtjs.dev/config-head
  head: {
    title: 'Geoffrey van Wyk',
    htmlAttrs: {
      lang: 'en',
    },
    bodyAttrs: {
      class: 'bg-repeat heropattern-circuitboard-gray-400',
    },
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: '' },
      { name: 'format-detection', content: 'telephone=no' },
    ],
    link: [{ rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }],
  },

  // Global CSS: https://go.nuxtjs.dev/config-css
  css: [],

  // Plugins to run before rendering page: https://go.nuxtjs.dev/config-plugins
  plugins: [],

  // Auto import components: https://go.nuxtjs.dev/config-components
  components: true,

  // Modules for dev and build (recommended): https://go.nuxtjs.dev/config-modules
  buildModules: [
    // https://go.nuxtjs.dev/typescript
    '@nuxt/typescript-build',
    // https://go.nuxtjs.dev/tailwindcss
    '@nuxtjs/tailwindcss',
    // TODO: Remove this function when tailwindcss-module adds support to v3
    function () {
      this.nuxt.hook('tailwindcss:config', (config) => {
        // Move the legacy purge content array to the the new property
        // https://tailwindcss.com/docs/upgrade-guide#configure-content-sources
        config.content = config.purge.content
        // Remove legacy purge option to disable the warning
        config.purge = undefined
      })
    },
  ],

  // Modules: https://go.nuxtjs.dev/config-modules
  modules: [
    // https://github.com/dword-design/nuxt-content-git
    'nuxt-content-git',
    // https://go.nuxtjs.dev/content
    '@nuxt/content',
  ],

  // Content module configuration: https://go.nuxtjs.dev/config-content
  content: {},

  // Build Configuration: https://go.nuxtjs.dev/config-build
  build: {},
  tailwindcss: {
    config: {
      plugins: [tailwindTypography, tailwindHeroPatterns],
    },
  },
}
