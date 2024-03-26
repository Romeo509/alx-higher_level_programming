#!/usr/bin/node

const fs = require('fs');

const [, , filePath, content] = process.argv;

if (typeof content !== 'string') {
    console.error(new Error('Content must be a string'));
    process.exit(1);
}

fs.writeFile(filePath, content, 'utf8', (err) => {
    if (err) {
        console.error(err);
        return;
    }
});