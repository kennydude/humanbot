var webpack = require("webpack");

module.exports = {
    entry: './app.js',
    output: {
        path: __dirname + '/static',
        filename: 'app.js'
    },
    module:{
        loaders: [
            {
                test: /\.html$/,
                loader: "underscore-template-loader",
                query: {
                    attributes: []
                }
            },
            // Switch on ES6 + ES7!
            { test: /\.js$/,
              exclude: /(node_modules)/,
              loader: 'babel-loader'
            }
        ]
    },
    resolve: {
        // Let's us do nice things like require("auth/views/login") etc
        root: __dirname
    },
    devtool: "#source-map"
}
