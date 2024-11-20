from typing import List


class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        n=len(prices)
        def maximum_profit(ind,buy):
            if ind==len(prices):
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            if buy:
                dp[ind][buy]=max(maximum_profit(ind+1,1),prices[ind]+maximum_profit(ind+1,0))
            else:
                dp[ind][buy]=max(maximum_profit(ind+1,0),-prices[ind]+maximum_profit(ind+1,1))
            return dp[ind][buy]
        dp=[[-1 for i in range(2)] for j in range(n)]
        return maximum_profit(0,0)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))
        solution = Solution()
        res = solution.maximumProfit(arr)
        print(res)

# } Driver Code Ends