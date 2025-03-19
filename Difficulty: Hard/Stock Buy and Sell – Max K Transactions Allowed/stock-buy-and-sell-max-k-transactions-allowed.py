class Solution:
    def maxProfit(self, prices, k):
        # code here
        def stocks(ind,buy,k):
            if ind==len(prices) or k==0:
                if buy==0:
                    return -float("inf")
                return 0
            if dp[ind][buy][k]!=-1:
                return dp[ind][buy][k]
            if buy:
                dp[ind][buy][k]=max(stocks(ind+1,1,k),-prices[ind]+stocks(ind+1,0,k))
                return dp[ind][buy][k]
            else:
                dp[ind][buy][k]=max(stocks(ind+1,0,k),prices[ind]+stocks(ind+1,1,k-1))
                return dp[ind][buy][k]
        dp=[[[-1 for _ in range(k+1)] for _ in range(2)] for _ in range(len(prices))]
        return stocks(0,1,k)

#{ 
 # Driver Code Starts
from collections import deque

if __name__ == "__main__":
    tc = int(input())
    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())
        obj = Solution()
        print(obj.maxProfit(arr, k))
        print("~")
# } Driver Code Ends