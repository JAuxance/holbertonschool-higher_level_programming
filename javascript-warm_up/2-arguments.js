#!bin/usr/node
const myVar = process.argv[2];
if (myVar === undefined) {
    console.log('No argument');
} else if (myVar.length > 1) {
    console.log('Arguments found');
} else {
    console.log('Argument found');
}
