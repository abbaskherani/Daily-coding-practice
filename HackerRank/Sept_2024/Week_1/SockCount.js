// const obj = {
//     10 : 1,
//     20:3
// }

// // console.log(obj[20])


// const sockCount = {}
// let pairs=0;

// for (let sock of [10,20,10,10,10,20,20,30,30,40]){
//     if(sockCount[sock]) 
//     {
//         sockCount[sock]++;
//         console.log(sockCount[sock])
//     }
//     else sockCount[sock] = 1;
// }
// console.log(sockCount)



function sockMerchant(n, ar) {
    
    //using hashmap to store key value
    const sockCount = {};
    let pairs = 0;

    // Count the frequency of each sock color
    for (let sock of ar) {
        if (sockCount[sock]) {
            sockCount[sock]++;
        } else {
            sockCount[sock] = 1;
        }
    }
console.log(sockCount)
    // Calculate the number of pairs for each color
    for (let color in sockCount) {
        pairs += Math.floor(sockCount[color] / 2);
    }

    return pairs;
}

console.log("pair of socks " + sockMerchant(9,[10 ,20 ,20 ,10 ,10 ,30 ,50, 10, 20]))
// STDIN                       Function
// -----                       --------
// 9                           n = 9
// 10 20 20 10 10 30 50 10 20  ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]