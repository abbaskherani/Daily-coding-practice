'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

/*
 * Complete the 'birthday' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER_ARRAY s
 *  2. INTEGER d
 *  3. INTEGER m
 */

function birthday(s, d, m) {
    // // Write your code here
    // //i =0 
    // for(let i=0;i<=m;i++)
    // if s[i]+ s[i+1] + s[i+2] ==d
    // // count++
    // arr[0]+arr[1] //s[i] + s[i+1] = d //count++
    // arr[1]+arr[2] // s[i+1] +s[i+2] = d
      let result = 0;
    
    for (let i = 0, l = s.length; i < l; i++) { //0, 5,i++ 
        if (s.slice(i, i + m).reduce((x, y) => x + y) === d) { //(0,2).(1+2) 
            result++;
        }
    }
    
    return result;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const n = parseInt(readLine().trim(), 10);

    const s = readLine().replace(/\s+$/g, '').split(' ').map(sTemp => parseInt(sTemp, 10));

    const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');

    const d = parseInt(firstMultipleInput[0], 10);

    const m = parseInt(firstMultipleInput[1], 10);

    const result = birthday(s, d, m);

    ws.write(result + '\n');

    ws.end();
}
