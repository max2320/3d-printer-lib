var path = require('path');
var webpack = require('webpack');

var srcPath = path.resolve(__dirname, 'src');
var destPath = path.resolve(__dirname, 'client');

module.exports = {
  entry: [
    path.resolve(srcPath, 'index.js'),
  ],
  output: {
    path: destPath,
    filename: 'bundle.js'
  },
  module: {
    loaders: [{ 
      test: /\.css$/, 
      use: [{
        loader: 'style-loader',
      },{
        loader: 'css-loader', 
        options: {
          importLoaders: 1, 
          camelCase: true, 
          modules: true
        }
      },{
        loader: 'postcss-loader',
        options: {
          plugins: (loader) => [
            require('postcss-import')({ root: loader.resourcePath }),
            require('postcss-cssnext')(),
            require('postcss-nested')()
          ]
        }
      }]
    },{ 
      test: /\.js(x)?$/, 
      exclude: /node_modules/, 
      loaders: ['babel-loader'] 
    },{ 
      test: /\.(png|jpg|svg)$/, 
      use: [{
        loader: 'url-loader', 
        options: {
          name:'images/[name].[ext]' 
        }
      }]
    }]
  },
  externals: {},
  plugins: [
    new webpack.LoaderOptionsPlugin({
      debug: true
    }),
  ]
};