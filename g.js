// let arr = ["apple", "mango", "apple",
//     "orange", "mango", "mango"];

// function removeDuplicates(arr) {
// return arr.filter(function (item,index){
//     console.log(item,index);
//     return arr.indexOf(item) === index;
// })
// }
// console.log(removeDuplicates(arr));



//always use below two pointer template for all codes using two pointer
const b = [1,1,2,2,1,1] //0..0 1 0..1 2 0..2 3
let k=4;
let sum = 0,count=0;
for(let i=0,j=0;j<b.length;j++){
    sum = sum + b[j];
    console.log("sum after b[j] ",sum)
    while(sum > k){
        sum = sum - b[i]
        console.log("inside while", sum)
        i++;
    }
    count += (j-i+1);
    console.log("j-i+1 is ",(j-i+1),"count is ",count)
}

console.log(count)