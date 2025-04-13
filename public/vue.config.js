//import { defineConfig } from '@vue/cli-service'
//export default defineConfig({
//  transpileDependencies: true
//})
const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    port: 5000, // Должен совпадать с port в launch.json
    proxy: {
      '/api': {
        target: 'http://127.0.0.1:8000', // Адрес вашего FastAPI бэкенда
        changeOrigin: true,
        pathRewrite: {
          '^/api': ''
        }
      }
    }
  }
})