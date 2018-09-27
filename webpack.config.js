const webpack = require('webpack');
const path = require('path');
const merge = require('webpack-merge');
const parts = require('./webpack/webpack.parts');

module.exports = merge([
  {
    mode: 'production',
    devtool: 'inline-source-map',
    entry: [
      `${__dirname}/client/index`,
    ],
    output: {
      path: __dirname,
      filename: `client/static/js/bundle.[hash].js`,
      publicPath: '/static/'
    },
  },
  parts.createManifest('manifest.json'),
  parts.bundleCSS(),
  parts.bundleSCSS(),
  parts.minifyJS(),
  parts.transpileJS(),
  parts.devServer('0.0.0.0', 5001),
]);
