#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 4) {
    console.error(new Error('Usage: ./1-writeme.js <file_path> <string_to_write>'));
    process.exit(1);
}

const [, , filePath, content] =process.argv;

fs.writeFile(filePath, content, 'utf8', (err) => {
    if (err) {
        console.error(err);
        return;
    }
    console.log('Content has been successfully written to  ${filePath}')
});
