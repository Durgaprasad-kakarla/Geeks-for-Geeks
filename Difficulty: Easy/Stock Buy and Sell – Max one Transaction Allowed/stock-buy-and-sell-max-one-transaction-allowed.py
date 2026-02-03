class Solution:
    def maxProfit(self, prices):
        # code here
        n=len(prices)
        maxi,mini=-float('inf'),float('inf')
        for i in range(n):
            mini=min(mini,prices[i])
            maxi=max(maxi,prices[i]-mini)
        return maxi