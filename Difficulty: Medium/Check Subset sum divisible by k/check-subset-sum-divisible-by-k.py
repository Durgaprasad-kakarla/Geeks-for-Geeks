class Solution:
    def divisibleByK(self, arr, k):
        # code here
        n = len(arr)
        dp = [[False] * k for _ in range(n + 1)]
        dp[0][0]=True
        for i in range( n):
            for j in range(k):
                if dp[i][j]:
                    dp[i+1][j]=True
                    rem=(j+arr[i])%k
                    if rem==0:
                        return True
                    dp[i+1][rem]=True
        return False