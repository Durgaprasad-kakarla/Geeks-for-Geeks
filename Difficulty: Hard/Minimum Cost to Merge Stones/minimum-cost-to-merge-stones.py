class Solution:
    def mergeStones(self, stones, k):
        # code here
        n = len(stones)
        if (n - 1) % (k - 1) != 0:
            return -1

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + stones[i]

        def get_sum(l, r):
            return pref[r + 1] - pref[l]

        INF = 10**15
        dp = [[[INF] * (k + 1) for _ in range(n)] for _ in range(n)]

        for i in range(n):
            dp[i][i][1] = 0

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1

                for t in range(2, k + 1):
                    for mid in range(i, j, k - 1):
                        if dp[i][mid][1] == INF or dp[mid+1][j][t-1] == INF:
                            continue
                        dp[i][j][t] = min(dp[i][j][t],
                                          dp[i][mid][1] + dp[mid+1][j][t-1])

                if dp[i][j][k] < INF:
                    dp[i][j][1] = dp[i][j][k] + get_sum(i, j)

        return dp[0][n-1][1]