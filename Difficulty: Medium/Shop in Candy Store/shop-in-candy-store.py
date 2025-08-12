class Solution:
    def minMaxCandy(self, prices, k):
        # code here
        prices.sort()
        n=len(prices)
        min_cost,remaining=0,n
        for i in range(n):
            if remaining>i:
                min_cost+=prices[i]
                remaining-=k
        remaining,max_cost=n,0
        for i in range(n-1,-1,-1):
            if remaining>(n-i-1):
                max_cost+=prices[i]
                remaining-=k
        return [min_cost,max_cost]
            