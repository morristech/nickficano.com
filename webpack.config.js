const webpack = require('webpack');
const path = require('path');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const ManifestPlugin = require('webpack-manifest-plugin');

module.exports = {
  mode: 'production',
  entry: [
    './client/index'
  ],
  output: {
    path: __dirname,
    filename: 'client/static/js/bundle.[hash].js',
    publicPath: '/static/'
  },
  resolve: {},
  devtool: 'eval-source-map',
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'client/static/css/[name].[hash].css',
      chunkFilename: 'client/static/css/[id].[hash].css',
    }),
    new ManifestPlugin({
      filename: 'manifest.json',
      publicPath: '/',
    })
  ],
  module: {
    rules: [
      {
        test: /\.css$/,
        use: [
          MiniCssExtractPlugin.loader,
          {
            // Inlining for simplicity, We do not want additional external files.
            loader: 'css-loader', // translates CSS into CommonJS
            options: {
              url: false,
              sourceMap: true,
            },
          },
        ],
      },
      {
        test: /\.scss$/,
        use: [
          MiniCssExtractPlugin.loader,
          {
            // Inlining for simplicity, We do not want additional external files.
            loader: 'css-loader', // translates CSS into CommonJS
            options: {
              url: false,
              sourceMap: true,
              minimize: true
            },
          },
          {
            loader: 'sass-loader', // compiles Sass to CSS
            options: {
              url: false,
              sourceMap: true,
              minimize: true
            },
          },
        ],
      },
    ],
  },
};