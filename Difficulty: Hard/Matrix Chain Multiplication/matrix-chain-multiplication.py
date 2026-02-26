class Solution:
    def matrixMultiplication(self, arr):
        # code here
        n=len(arr)
        dp=[[float('inf') for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n):
            dp[i][i]=0
        for d in range(1,n-1):
            for i in range(1,n):
                j=i+d
                if j>=n:
                    break
                mini=float('inf')
                for k in range(i,j):
                    mini=min(mini,arr[i-1]*arr[k]*arr[j]+dp[i][k]+dp[k+1][j])
                dp[i][j]=mini
        return dp[1][n-1]
        