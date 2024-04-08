#User function Template for python3


#Function to find the maximum possible amount of money we can win.
class Solution:
    def optimalStrategyOfGame(self,n, arr):
        # code here
        def func(i,j,dp):
            if i>j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            l=arr[i]+min(func(i+2,j,dp),func(i+1,j-1,dp))
            r=arr[j]+min(func(i,j-2,dp),func(i+1,j-1,dp))
            dp[i][j]=max(l,r)
            return max(l,r)
        dp=[[-1 for i in range(n)] for j in range(n)]
        return func(0,n-1,dp)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int,input().strip().split()))
        ob = Solution()
        print(ob.optimalStrategyOfGame(n,arr))

# } Driver Code Ends