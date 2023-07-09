const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    allowedHosts: 'all',
    proxy: process.env.VUE_APP_PROXY_BASE_URL,
  },
  assetsDir: 'static'
})
