//Find maximum number of a type of bird

function migratoryBirds(arr) {
    // Write your code here
//    let hashmap ={};

const birdCount = Array(6).fill(0);
   for (let bird of arr){
       birdCount[bird]++
   }
   const max = birdCount.indexOf(Math.max(...birdCount))
  
return max;
}


console.log(migratoryBirds([1,4,4,4,2,3,3]))

// The different types of birds occur in the following frequencies:

// Type 1 : 1 bird
// Type 2: 0 birds
// Type 3: 2 bird
// Type 4: 3 birds
// Type 5: 1 bird
// The type number that occurs at the highest frequency is type , so we print  as our answer.


//output -------- 4