class Solution:
    def countConsec(self, n: int) -> int:
        # code here 
        dp=[0]*(n+1)
        dp[2]=1
        for i in range(3,n+1):
            dp[i]=(dp[i-1]+(2**(i-2)+dp[i-2]))
        return dp[n]