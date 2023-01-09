const webpack = require('webpack');
const { merge } = require('webpack-merge');
const common = require('./webpack.common');

module.exports = merge(common, {
    mode: 'production',
    entry: {
        app: './index.js'
    },
    module: {
        rules: [
            {
                test: /\.ya?ml$/,
                use: 'yaml-loader'
            }
        ]
    },
});