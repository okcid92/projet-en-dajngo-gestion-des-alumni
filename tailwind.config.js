/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./alumni/templates/**/*.{html,js}",
    "./alumni/static/**/*.{html,js}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#fff7ed',
          100: '#ffedd5',
          200: '#fed7aa',
          300: '#fdba74',
          400: '#fb923c',
          500: '#f97316', // Orange/Coral
          600: '#ea580c',
          700: '#c2410c',
          800: '#9a3412',
          900: '#7c2d12',
          DEFAULT: '#ea663b', // IBAM Original
        },
        secondary: {
          50: '#fffcfb',
          100: '#fff4f1',
          200: '#ffe3db',
          300: '#ffcab8',
          400: '#ffa78c',
          500: '#f0906e', // Original Secondary
          600: '#e86d42',
          700: '#d14f24',
          800: '#b03f1b',
          900: '#913518',
        },
        info: {
          50: '#f0f9ff',
          100: '#e0f2fe',
          200: '#bae6fd',
          300: '#7dd3fc',
          400: '#38bdf8',
          500: '#42b5da', // Original Info
          600: '#0284c7',
          700: '#0369a1',
          800: '#075985',
          900: '#0c4a6e',
        },
        accent: {
          DEFAULT: '#F30C05',
        },
        dark: {
          50: '#f8fafc',
          100: '#f1f5f9',
          200: '#e2e8f0',
          300: '#cbd5e1',
          400: '#94a3b8',
          500: '#64748b',
          600: '#475569',
          700: '#334155',
          800: '#1e293b',
          900: '#0f172a',
          950: '#020617',
          DEFAULT: '#000000',
        },
        light: {
          DEFAULT: '#f8f9fa',
        }
      },
      fontFamily: {
        sans: ['Inter', 'ui-sans-serif', 'system-ui', '-apple-system', 'BlinkMacSystemFont', 'Segoe UI', 'Roboto', 'Helvetica Neue', 'Arial', 'sans-serif'],
      },
      boxShadow: {
        'soft': '0 2px 15px -3px rgba(0, 0, 0, 0.07), 0 10px 20px -2px rgba(0, 0, 0, 0.04)',
      }
    },
  },
  plugins: [],
}

