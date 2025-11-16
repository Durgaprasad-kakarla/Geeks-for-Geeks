class Solution:
    def LCIS(self, a, b):
        # code here
        n,m=len(a),len(b)
        dp=[0 for i in range(m)]
        for i in range(n):
            curr_max=0
            for j in range(m):
                if a[i]==b[j]:
                    dp[j]=1+curr_max
                elif b[j]<a[i]: 
                    curr_max=max(curr_max,dp[j])
        # print(dp)
        return max(dp)
        
        