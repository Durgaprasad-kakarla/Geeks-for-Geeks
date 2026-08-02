class Solution:
    def count(self, n: int, m: int) -> int:
        # code here
        def count(cur,n):
            # print(cur,prev,n)
            if n==0:
                return 1
            if dp[cur+1][n]!=-1:
                return dp[cur+1][n]
            cnt=0
            for i in range(1,m+1):
                if cur==-1 or (i%cur==0 or cur%i==0):
                    cnt+=count(i,n-1)
            dp[cur+1][n]=cnt
            return cnt
        dp=[[-1 for _ in range(n+1)] for _ in range(m+2)]
        return count(-1,n)