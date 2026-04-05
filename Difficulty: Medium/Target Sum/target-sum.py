class Solution:
    def totalWays(self, arr, target):
        # code here
        def total_ways(ind,target):
            if target==0:
                return 1
            if ind<0:
                return 0
            if dp[ind][target]!=-1:
                return dp[ind][target]
            l=0
            if target>=arr[ind]:
                l=total_ways(ind-1,target-arr[ind])
            r=total_ways(ind-1,target)
            dp[ind][target]=l+r
            return dp[ind][target]
        d=sum(arr)+target
        if d%2!=0:
            return 0
        d=d//2
        n=len(arr)
        dp=[[-1 for _ in range(d+1)] for _ in range(n)]
        return total_ways(n-1,d)