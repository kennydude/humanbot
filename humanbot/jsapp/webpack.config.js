var webpack = require("webpack");

module.exports = {
    entry: './app.js',
    output: {
        path: __dirname + '/static',
        filename: 'app.js'
    },
    resolve: {
        extensions: ['', '.js', '.jsx']
    },
    module:{
        loaders: [
            // Switch on ES6 + ES7!
            {
                test: /\.jsx?$/,
                exclude: /(node_modules)/,
                loaders: ['babel?cacheDirectory'],
            },
            {
                test: /\.json$/,
                loaders: ['json']
            }
        ]
    },
    resolve: {
        // Let's us do nice things like require("auth/views/login") etc
        root: __dirname,
    },
    devtool: "#source-map"
}
