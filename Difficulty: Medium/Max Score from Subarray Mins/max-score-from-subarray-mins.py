class Solution:
    def maxSum(self, arr):
        # code here
        n=len(arr)
        sm=arr[0]+arr[1]
        maxi=sm
        for i in range(2,n):
            sm+=(arr[i]-arr[i-2])
            maxi=max(maxi,sm)
        return maxi
        
        
    
