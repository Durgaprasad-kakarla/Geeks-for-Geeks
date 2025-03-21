class Solution:  
    def findMaxSum(self,arr):
        # code here
        n=len(arr)
        dp=[0]*(n+1)
        dp[1]=arr[0]
        for i in range(2,n+1):
            l=dp[i-1]
            r=-float("inf")
            if i>1:
                r=dp[i-2]+arr[i-1]
            dp[i]=max(l,r)
        return dp[-1]

#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**6)

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):

        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.findMaxSum(a))
        print("~")

# } Driver Code Ends