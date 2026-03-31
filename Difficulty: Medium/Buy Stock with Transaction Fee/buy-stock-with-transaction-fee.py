class Solution:
    def maxProfit(self, arr, k):
        # Code here
        def max_profit(ind,buy):
            if ind==n:
                return 0
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            if buy:
                dp[ind][buy]= max(max_profit(ind+1,0)-arr[ind],max_profit(ind+1,1))
            else:
                dp[ind][buy]= max(max_profit(ind+1,1)+arr[ind]-k,max_profit(ind+1,0))
            return dp[ind][buy]
        n=len(arr)
        dp=[[-1 for _ in range(0,2)] for _ in range(n)]
        return max_profit(0,1)