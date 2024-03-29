/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./themes/windy/templates/**/*.html', './theme/windy/assets/**/*.css'],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/typography'),
    require('tailwindcss-hero-patterns'),
    require('tailwind-fontawesome')({
      version: 6
    })],
}

