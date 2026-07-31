class Solution:
    def matrixMultiplication(self, arr):
        # code here
        n=len(arr)
        def matrix_chain(i,j):
            if i==j:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            mini=float('inf')
            for k in range(i,j):
                mini=min(mini,(arr[i-1]*arr[k]*arr[j])+matrix_chain(i,k)+matrix_chain(k+1,j))
            dp[i][j]=mini
            return mini
        dp=[[-1 for _ in range(n)] for _ in range(n)]
        return matrix_chain(1,n-1)
        