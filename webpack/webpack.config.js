const webpack = require('webpack');
const path = require('path');
const merge = require('webpack-merge');
const parts = require('./webpack.parts');

const common = merge([
  parts.createManifest('manifest.json'),
  parts.bundleCSS(),
  parts.bundleSCSS(),
]);

const production = merge([
  {
    mode: 'production',
    devtool: 'source-map',
  },  
  {
    entry: [
      `${path.join(__dirname, '..')}/client/index`,
    ],
  },
  {
    output: {
      path: path.join(__dirname, '..'),
      filename: '../client/static/js/bundle.[hash].js',
      publicPath: '/static/'
    },
  },  
  parts.minifyJS(),
]);

module.exports = merge(common, production);