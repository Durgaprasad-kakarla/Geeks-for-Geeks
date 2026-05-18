class Solution:
    def maxSum(self, n):
        # code here
        def func(n):
            if n<=1:
                return 0
            if dp[n]!=-1:
                return dp[n]
            l=max(n//2,func(n//2))
            r=max(n//3,func(n//3))
            k=max(n//4,func(n//4))
            dp[n]=l+r+k
            return l+r+k
        dp=[-1 for _ in range(n+1)]
        return max(n,func(n))
                    