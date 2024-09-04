/*
 * Complete the 'divisibleSumPairs' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER k
 *  3. INTEGER_ARRAY ar
 */

function divisibleSumPairs(n, k, ar) {
    // Write your code here
    let count=0
    for(let i=0;i<n;i++){
        for(let j=i+1;j<n;j++){
            // console.log(ar[i],ar[j]);
            if ((ar[i]+ar[j])% k == 0){
                // console.log(ar[i],ar[j])
               count++; 
            }
        }
    }
return count;
}


console.log(divisibleSumPairs(5,3,[1,2,2,1,4,5]))