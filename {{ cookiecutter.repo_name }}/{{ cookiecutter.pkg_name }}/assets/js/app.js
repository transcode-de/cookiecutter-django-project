/*global $*/

import '../scss/app.scss'

// Some of Foundation's JavaScript modules can't be loaded as a CommonJS
// module. This GitHub issue[1] deals with it, this Stack Overflow page[2]
// contains a few different solutions for it.
//
// [1] https://github.com/zurb/foundation-sites/issues/7386
// [2] https://stackoverflow.com/questions/34297788/npm-zurb-foundation-webpack-cannot-resolve-module-foundation/34611081
import 'script!jquery'
import 'script!what-input'
import 'script!foundation-sites'

$(document).ready(function () {
  $(document).foundation()
})
