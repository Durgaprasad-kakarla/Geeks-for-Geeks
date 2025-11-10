class Solution:
    def maxProfit(self, arr):
        # code here
        def buy_sell_stocks(ind,buy):
            if ind>=n:
                if buy:
                    return 0
                return -float('inf')
            if dp[ind][buy]!=-1:
                return dp[ind][buy]
            if buy:
                maxi=max(buy_sell_stocks(ind+1,0)-arr[ind],buy_sell_stocks(ind+1,1))
            else:
                maxi=max(arr[ind]+buy_sell_stocks(ind+2,1),buy_sell_stocks(ind+1,0))
            dp[ind][buy]=maxi
            return maxi
        n=len(arr)
        dp=[[-1 for i in range(2)] for _ in range(n)]
        ans=buy_sell_stocks(0,1)
        return ans
        