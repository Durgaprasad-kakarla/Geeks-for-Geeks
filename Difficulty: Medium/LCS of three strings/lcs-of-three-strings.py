class Solution:
    def lcsOf3(self,s1, s2, s3):
        # Code here
        n1,n2,n3=len(s1),len(s2),len(s3)
        def lcs(ind1,ind2,ind3,s1,s2,s3,dp):
            if ind1<0 or ind2<0 or ind3<0:
                return 0
            if dp[ind1][ind2][ind3]!=-1:
                return dp[ind1][ind2][ind3]
            if s1[ind1]==s2[ind2] and s1[ind1]==s3[ind3]:
                dp[ind1][ind2][ind3]=1+lcs(ind1-1,ind2-1,ind3-1,s1,s2,s3,dp)
                return dp[ind1][ind2][ind3]
            dp[ind1][ind2][ind3]=max(lcs(ind1-1,ind2,ind3,s1,s2,s3,dp),lcs(ind1,ind2-1,ind3,s1,s2,s3,dp),lcs(ind1,ind2,ind3-1,s1,s2,s3,dp))
            return dp[ind1][ind2][ind3]
        dp=[[[-1 for i in range(n3)] for j in range(n2)] for k in range(n1)]
        return lcs(n1-1,n2-1,n3-1,s1,s2,s3,dp)