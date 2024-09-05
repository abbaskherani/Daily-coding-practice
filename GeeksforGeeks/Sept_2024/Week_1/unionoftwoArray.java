class Solution {
    public static int doUnion(int arr1[], int arr2[]) {
        // Your code here
        Set<Integer> union = new HashSet<>();
        
        for(int i=0;i<arr1.length;i++){
            union.add(arr1[i]);
        }
        for(int i=0;i<arr2.length;i++){
            union.add(arr2[i]);
        }
    return union.size();
    }
}