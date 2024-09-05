//to find unique elements in both the array and then print how many element it has
class Solution {
    // Function to return the count of number of elements in the union of two arrays.
    doUnion(arr1, arr2) {
        // code here
       const newArray = [...arr1,...arr2];
       
       const set1 = new Set(newArray);
       
       return set1.size;
    }
}