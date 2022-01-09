const path = require('path');
const MiniCSSExtractPlugin = require('mini-css-extract-plugin');

module.exports = {
    entry: {
        'wagtailiconify_fontawesome': path.resolve(__dirname, 'wagtailiconify/develop/scss/wagtailiconify_fontawesome.scss'),
    },
    output: {
        path: path.resolve(__dirname, 'wagtailiconify/static/wagtailiconify/css'),
    },
    plugins: [
        new MiniCSSExtractPlugin({
            filename: '[name].min.css'
        })
    ],
    module: {
        rules: [
            {
                test: /\.s?css$/,
                use: [
                    MiniCSSExtractPlugin.loader,
                    "css-loader",
                    "sass-loader"
                ]
            },
        ]
    }

}