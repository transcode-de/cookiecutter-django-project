var autoprefixer = require('autoprefixer')
var path = require('path')

module.exports = {
  context: __dirname,
  entry: [
    './{{ cookiecutter.pkg_name }}/assets/js/app.js'
  ],
  output: {
    path: path.resolve('./{{ cookiecutter.pkg_name }}/static/bundles/'),
    filename: '[name]-[hash].js'
  },
  plugins: [],
  module: {
    loaders: [
      {
        test: /\.js$/,
        exclude: /(node_modules)/,
        loader: 'babel',
        query: {
          presets: ['es2015']
        }
      },
      {
        test: /\.scss$/,
        loader: 'style!css!postcss!sass'
      }
    ]
  },
  postcss: [
    autoprefixer({
      browsers: ['last 2 versions']
    })
  ],
  sassLoader: {
    includePaths: [
      path.resolve(__dirname, 'node_modules/foundation-sites/scss/')
    ]
  }
}
