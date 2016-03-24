var BundleTracker = require('webpack-bundle-tracker')
var config = require('./webpack.base.config.js')
var webpack = require('webpack')

config.plugins = config.plugins.concat([
  new BundleTracker({
    filename: './{{ cookiecutter.pkg_name }}/webpack-stats.json'
  }),
  new webpack.optimize.OccurenceOrderPlugin(),
  new webpack.optimize.UglifyJsPlugin({
    compressor: {
      warnings: false
    }
  })
])

module.exports = config
