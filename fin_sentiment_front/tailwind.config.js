module.exports = {
  purge: ['./src/**/*.{js,jsx,ts,tsx}', './public/index.html'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      fontFamily: {
        ProximaNova: ["Proxima Nova"],
      },
      minHeight: {
        '36': '9rem',
       },
       maxHeight:{
         '10':'2.5rem',
       },
       scale: {
         '101':'1.01'
       }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
