//find if element if greater that its neighbor elements

class Solution
{
	// Function to find the peak element
	// arr[]: input array
	// n: size of array a[]
	public int peakElement(int[] arr,int n)
    {
       //add code here.
       if(n==1 || arr[0]>=arr[1])
       {return 0;}
       
      if(arr[n-1]>=arr[n-2])
      {return n-1;}
      
      for(int i=1;i<n;i++){
          if(arr[i]>=arr[i-1] && arr[i]>=arr[i+1])
            {return i;}
      }
      return -1;
    }
}