/*eslint no-console: ["error", { allow: ["warn", "error"] }] */

var fs = require('fs');
var CleanCSS = require('clean-css');

const sources = [
    './assets/css/normalize.css',
    './assets/css/zenkai.css',
    './assets/css/base.css',
    './assets/css/style.css',
];


const bundle = new CleanCSS({
    sourceMap: true,
    rebaseTo: `./dist/style.min.css`
}).minify(sources);

// log bundle result
outputFeedback(bundle.errors, true);
outputFeedback(bundle.warnings);

// write bundle file
// if (!fs.existsSync(DIRECTORY)) {
//     fs.mkdirSync(DIRECTORY, { recursive: true });
// }

// write bundle file
output({ path: `./dist/style.min.css` }, bundle.styles);
output({ path: `./dist/style.min.map` }, bundle.sourceMap.toString());

function outputFeedback(messages, isError) {
    var prefix = isError ? '\x1B[31mERROR\x1B[39m:' : 'WARNING:';

    messages.forEach(function (message) {
        console.error('%s %s', prefix, message);
    });
}

function output(options, minified) {
    fs.writeFileSync(options.path, minified, 'utf8');
}