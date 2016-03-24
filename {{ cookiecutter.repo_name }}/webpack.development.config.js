var BrowserSyncPlugin = require('browser-sync-webpack-plugin')
var BundleTracker = require('webpack-bundle-tracker')
var config = require('./webpack.base.config.js')
var path = require('path')

config.output.path = path.resolve('./{{ cookiecutter.pkg_name }}/static/bundles-development/')

config.plugins = config.plugins.concat([
  new BundleTracker({
    filename: './{{ cookiecutter.pkg_name }}/webpack-stats-development.json'
  }),
  new BrowserSyncPlugin(
    // BrowserSync options
    {
      host: 'localhost',
      port: 3000,
      proxy: 'http://localhost:8000/',
      files: [
        './webpack*.config.js',
        './{{ cookiecutter.pkg_name }}/**/*.py',
        './{{ cookiecutter.pkg_name }}/templates/**/*.html',
        './{{ cookiecutter.pkg_name }}/webpack-stats-development.json'
      ],
      // Wait until Django's runserver has restarted.
      reloadDelay: 2000,
      online: false,
      open: false
    },
    // plugin options
    {}
  )
])

module.exports = config
