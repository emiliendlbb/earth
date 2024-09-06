/**
 * dev-server - serves static resources for developing "earth" locally
 */

"use strict";

console.log("============================================================");
console.log(new Date().toISOString() + " - Starting");

var util = require("util");
var express = require("express");
var compression = require('compression');
var morgan = require('morgan');

var app = express();

/**
 * Returns true if the response should be compressed.
 */
function compressionFilter(req, res) {
    return (/json|text|javascript|font/).test(res.getHeader('Content-Type'));
}

/**
 * Adds headers to a response to enable caching.
 */
function cacheControl() {
    return function(req, res, next) {
        res.setHeader("Cache-Control", "public, max-age=300");
        return next();
    };
}

// Define custom tokens for Morgan
morgan.token('date', function() {
    return new Date().toISOString();
});
morgan.token('response-all', function(req, res) {
    return (res._header ? res._header : "").trim();
});
morgan.token('request-all', function(req, res) {
    return util.inspect(req.headers);
});

// Configure Morgan logging
app.use(morgan(':date - info: :remote-addr :method :url HTTP/:http-version ":user-agent" :referrer :response-time ms\\n:request-all\\n\\n:response-all\\n'));

app.use(cacheControl());
app.use(compression({ filter: compressionFilter }));
app.use(express.static("public"));

var port = process.argv[2];
app.listen(port, () => {
    console.log("Listening on port " + port + "...");
});
