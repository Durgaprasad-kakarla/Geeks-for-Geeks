class Solution:
    def noOfWays(self, m,n,x):
        # code here
        def dice_throws(ind,x):
            if x<0:
                return 0
            if ind==0:
                if x==0:
                    return 1
                return 0
            if dp[ind][x]!=-1:
                return dp[ind][x]
            cnt=0
            for i in range(1,m+1):
                cnt+=dice_throws(ind-1,x-i)
            dp[ind][x]=cnt
            return cnt
        dp=[[-1 for _ in range(x+1)] for _ in range(n+1)]
        return dice_throws(n,x)