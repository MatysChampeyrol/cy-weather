import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: '/cy-weather/',  // Nom de votre repo
  build: {
    outDir: '../docs',    // Build dans docs/ à la racine
    emptyOutDir: true
  }
})
