const ManifestPlugin = require('webpack-manifest-plugin');
exports.createManifest = (filename) => ({
  plugins: [
    new ManifestPlugin({
      filename: filename,
      publicPath: '/',
    }),
  ],
});

const path = require('path');
const webpack = require('webpack');
exports.devServer = (host, port) => ({
  devServer: {
    compress: true,
    host,
    port,
    disableHostCheck: true,
    hot: true,
    historyApiFallback: true,
    overlay: true,
    proxy: {
      '/': {
        target: 'http://localhost:5000',
        secure: false,
      },
    },
  },
  output: {
    path: __dirname,
    filename: `client/static/js/bundle.js`,
    publicPath: '/static/'
  },  
  plugins: [
    new webpack.HotModuleReplacementPlugin(),
    new webpack.WatchIgnorePlugin([path.join(__dirname, 'node_modules')]),
    new MiniCssExtractPlugin({
      filename: 'client/static/css/[name].css',
    }),
  ],   
});

exports.transpileJS = () => ({
  module: {
    rules: [
      {
        test: /\.js/,
        exclude: /(node_modules)/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env'],
            plugins: [require('@babel/plugin-proposal-object-rest-spread')]
          }
        }
      }
    ]
  }  
});

const UglifyWebpackPlugin = require('uglifyjs-webpack-plugin');
exports.minifyJS = () => ({
  optimization: {
    minimizer: [
      new UglifyWebpackPlugin({
        sourceMap: true,
        extractComments: true,
      }),
    ]
  }
});

const MiniCssExtractPlugin = require('mini-css-extract-plugin');
exports.bundleCSS = ({ include, exclude } = {}) => ({
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'client/static/css/[name].[hash].css',
      chunkFilename: 'client/static/css/[id].[hash].css',
    }),
  ],
  module: {
    rules: [
      {
        test: /\.css$/,
        include,
        exclude,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
            options: {
              url: false,
              sourceMap: true,
            },
          },
        ],
      },
    ]
  }
});

exports.bundleSCSS = ({ include, exclude } = {}) => ({
  plugins: [
    new MiniCssExtractPlugin({
      filename: 'client/static/css/[name].[hash].css',
      chunkFilename: 'client/static/css/[id].[hash].css',
    }),
  ],
  module: {
    rules: [
      {
        test: /\.scss$/,
        include,
        exclude,
        use: [
          MiniCssExtractPlugin.loader,
          {
            loader: 'css-loader',
            options: {
              url: false,
              sourceMap: true,
              minimize: true
            },
          },
          {
            loader: 'sass-loader',
            options: {
              url: false,
              sourceMap: true,
              minimize: true
            },
          },
        ],
      },
    ]
  }
});
