/** @type {import('tailwindcss').Config} */
export default {
	darkMode: 'class',
	content: ['./src/**/*.{html,js,svelte,ts}'],
	theme: {
		extend: {
			colors: {
				gray: {
					50: '#f9f9f9',
					100: '#ececec',
					200: '#e3e3e3',
					250: '#d8d8d8',
					300: '#cdcdcd',
					400: '#b4b4b4',
					500: '#9b9b9b',
					600: '#676767',
					700: '#4e4e4e',
					800: '#333',
					850: '#262626',
					900: 'var(--color-gray-900, #171717)',
					950: 'var(--color-gray-950, #0d0d0d)'
				},
				primary: {
					darkest: '#00001e',
					lightdarkest: '#000025',
					dark:'#00002d',
					lightdark: '#000035',
					med: '#00003c',
					lightmedium: '#486f99',
					light:'#2a2a5c',
					lightest:'#7e7e9d'
				},
				secondary: {
					darkest: '#624411',
					dark:'#c0964d',
					medium: '#d4ad68',
					light:'#dbbb81',
					lightest:'#e9d6b3'
				},
				support: {
					lightblue: "#c4dbe5"
				},
				darktheme:{
					darkest: "#000003",
					dark: "#161b26",
					med: "#3f3f3f",
					light: "#636c78",
					lightest: "#c6c3c3",
					blue: "#080939"
				}
			},
			typography: {
				DEFAULT: {
					css: {
						pre: false,
						code: false,
						'pre code': false,
						'code::before': false,
						'code::after': false
					}
				}
			}
		}
	},
	plugins: [require('@tailwindcss/typography')]
};