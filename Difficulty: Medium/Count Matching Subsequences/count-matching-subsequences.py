class Solution:
    def countWays(self, s1, s2):
        # code here
        def count_ways(ind1,ind2):
            if ind2<0:
                return 1
            if ind1<0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if s1[ind1]==s2[ind2]:
                dp[ind1][ind2]= count_ways(ind1-1,ind2-1)+count_ways(ind1-1,ind2)
                return dp[ind1][ind2]
            dp[ind1][ind2]= count_ways(ind1-1,ind2)
            return dp[ind1][ind2]
        mod=10**9+7
        n,m=len(s1),len(s2)
        dp=[[-1 for _ in range(m)] for _ in range(n)]
        return count_ways(n-1,m-1)%mod
        
