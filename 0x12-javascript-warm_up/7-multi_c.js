#!/usr/bin/node

let occur = Number.parseInt(process.argv[2]);

if (Number.isInteger(occur))
{
    while (occur > 0)
    {
	console.log('C is fun');
	occur--;
    }
} else {
    console.log('Missing number of occurrences');
}
