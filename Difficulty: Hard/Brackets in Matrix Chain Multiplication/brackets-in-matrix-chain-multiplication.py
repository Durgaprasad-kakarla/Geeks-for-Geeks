class Solution:
    matrix = 'A'
    ans = ""

    def matrixChainOrder(self, p):
        # code here
        n=len(p)
        self.matrix = 'A'
        self.ans = ""
        dp = [[0 for _ in range(n)] for _ in range(n)]
        path = [[0 for _ in range(n)] for _ in range(n)]

        for pair in range(2, n):
            for i in range(1, n - pair + 1):
                j = i + pair - 1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    temp = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                    if temp < dp[i][j]:
                        dp[i][j] = temp
                        path[i][j] = k

        self.dfs(1, n - 1, path)
        return self.ans

    def dfs(self, i, j, path):
        if i == j:
            self.ans += self.matrix
            self.matrix = chr(ord(self.matrix) + 1)
            return

        self.ans += '('
        self.dfs(i, path[i][j], path)
        self.dfs(path[i][j] + 1, j, path)
        self.ans += ')'