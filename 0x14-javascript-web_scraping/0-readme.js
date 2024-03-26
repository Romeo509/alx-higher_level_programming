#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 3) {
    console.error(new Error('Incorreect number of arguments'));
    process.exit(1);
}

const [, , filePath] = process.argv;

fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file: ${err.message}');
        return;
    }

    console.log(data);
});
