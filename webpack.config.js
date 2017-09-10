const webpack = require('webpack');
const path = require('path');

const config = {
  entry: [
    './client/index'
  ],
  output: {
    path: __dirname,
    filename: 'client/static/js/bundle.js',
    publicPath: '/static/'
  },
  resolve: {},
  devtool: 'eval-source-map',
  plugins: [],
  module: {
    rules: [{
      test: /\.scss$/,
      loaders: ['style-loader', 'css-loader', 'sass-loader']
    }]
  },
};

module.exports = config;
