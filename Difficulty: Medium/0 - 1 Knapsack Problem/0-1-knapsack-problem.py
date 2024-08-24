#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val):
       
        def func(ind,W,dp):
            if ind<0:
                return 0
            if dp[ind][W]!=-1:
                return dp[ind][W]
            l=-float('inf')
            if W>=wt[ind]:
                l=val[ind]+func(ind-1,W-wt[ind],dp)
            r=func(ind-1,W,dp)
            dp[ind][W]=max(l,r)
            return max(l,r) 
        dp=[[-1 for i in range(W+1)] for j in range(len(wt))]
        return func(len(wt)-1,W,dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        # n = int(input())
        W = int(input())
        val = list(map(int, input().strip().split()))
        wt = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.knapSack(W, wt, val))

# } Driver Code Ends