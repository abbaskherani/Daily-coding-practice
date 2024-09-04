//to find if the person is fairly charge or overcharged
// if a person is not eaten that thing he or she should not be charged for it

function bonAppetit(bill, didnoteat, bCharged) {
    // Write your code here
    let bactual = bill.reduce((acc,curr) =>{return acc + curr;},0) - bill[didnoteat];
    bactual /=2;
   console.log( bCharged ==bactual ? 'Bon Appetit' : bCharged-bactual)
}

bonAppetit([3,10,2,9], 1, 9) //arr, arr index did not eat, charged value

//return the extra charged difference or else print bon appetit



// 4 1
// 3 10 2 9
// 12
// Sample Output

// 5