class Solution:
    def noOfWays(self, m,n,x):
        # code here
        def find_ways(ind,target):
            if ind==0:
                if target==0:
                    return 1
                return 0
            if dp[ind][target]!=-1:
                return dp[ind][target]
            cnt=0
            for i in range(1,m+1):
                if target>=i:
                    cnt+=find_ways(ind-1,target-i)
            dp[ind][target]=cnt
            return cnt
        dp=[[-1 for i in range(x+1)] for j in range(n+1)]
        return find_ways(n,x)