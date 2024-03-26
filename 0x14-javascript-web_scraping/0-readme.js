#!/usr/bin/node

const fs = require('fs');

if (process.argv.length !== 3) {
    console.error(new Error('Incorrect number of arguments'));
    process.exit(1);
}

const filePath = process.argv[2];

fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err.message);
        return;
    }

    console.log(data);

    fs.writeFile(filePath, data, 'utf8', (err) => {
        if (err) {
            console.error('Error writing file:', err);
            return;
        }
    });
});
