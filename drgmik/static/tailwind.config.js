const defaultTheme = require('tailwindcss/defaultTheme')

module.exports = {
  content: [
    "../templates/drgmik/*.html",
    "../../builder/templates/builder/*.html",
    "../../blog/templates/blog/*.html",
  ],
  theme: {
    colors: {
      'dark': {
        900: '#1e2228',
        500: '#282c34'
      },
      'light': {
        900: '#abb2bf',
        500: '#e5e5e5'
      },
      'red': '#e06c75',
      'green': '#98c379',
      'yellow': '#e5c07b',
      'blue': '#61afef',
      'purple': '#c678dd',
      'teal': '#56b6c2'
    },
    extend: {
      boxShadow: {
        'md': 'rgba(0, 0, 0, 1) 5.5px 5px',
        'lg': 'rgba(0, 0, 0, 1) 7px 6px'
      },
      fontFamily: {
        'mono': ['"3270 Semi-Narrow"', ...defaultTheme.fontFamily.mono]
      },
    },
    container: {
      center: true,
    },
    screens: {
      'sm': '200px',
      // => @media (min-width: 640px) { ... }

      'md': '300px',
      // => @media (min-width: 768px) { ... }

      'lg': '500px',
      // => @media (min-width: 1024px) { ... }

      'xl': '700px',
      // => @media (min-width: 1280px) { ... }

      '2xl': '900px',
      // => @media (min-width: 1536px) { ... }
    }
  }
}
