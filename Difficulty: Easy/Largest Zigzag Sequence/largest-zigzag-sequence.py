class Solution:
    def zigzagSequence(self, mat):
        # code here
        def zig_zag(ind,prev):
            if ind==0:
                maxi=0
                for i in range(n):
                    if i!=prev:
                        maxi=max(maxi,mat[ind][i])
                return maxi
            if dp[ind][prev+1]!=-1:
                return dp[ind][prev+1]
            maxi=0
            for i in range(n):
                if i!=prev:
                    maxi=max(maxi,mat[ind][i]+zig_zag(ind-1,i))
            dp[ind][prev+1]=maxi
            return maxi
        dp=[[-1 for _ in range(n+1)] for _ in range(n)]
        return zig_zag(n-1,-1)