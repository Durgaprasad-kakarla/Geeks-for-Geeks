#Back-end complete function Template for Python 3

class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        def mincost(ind):
            if ind<=1:
                return cost[ind]
            if ind<0:
                return float('inf')
            if dp[ind]!=-1:
                return dp[ind]
            l=mincost(ind-1)+cost[ind]
            r=float('inf')
            if ind>1:
                r=mincost(ind-2)+cost[ind]
            dp[ind]=min(l,r)
            return min(l,r)
        n=len(cost)
        dp=[-1]*n
        return min(mincost(n-1),mincost(n-2))
                


#{ 
 # Driver Code Starts
t = int(input())
for _ in range(t):
    arr = list(map(int, input().split()))  # Input array
    obj = Solution()
    res = obj.minCostClimbingStairs(arr)
    print(res)
    print("~")

# } Driver Code Ends