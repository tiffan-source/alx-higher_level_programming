#!/usr/bin/node

const { readFileSync, writeFileSync } = require('fs');

const text1 = readFileSync(process.argv[2]);
const text2 = readFileSync(process.argv[3]);

writeFileSync(process.argv[4], text1 + text2);
