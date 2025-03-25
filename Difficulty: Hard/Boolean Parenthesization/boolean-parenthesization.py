#User function Template for python3
class Solution:
    def countWays(self, s):
        # code here
        n=len(s)
        def solve(s, i, j, isTrue, dp):
            if i > j:
                return 0
            if i == j:
                return 1 if s[i] == ('T' if isTrue == 1 else 'F') else 0
            if dp[i][j][isTrue] != -1:
                return dp[i][j][isTrue]
        
            temp_ans = 0
            for k in range(i + 1, j, 2):
                lt = solve(s, i, k - 1, 1, dp)
                lf = solve(s, i, k - 1, 0, dp)
                rt = solve(s, k + 1, j, 1, dp)
                rf = solve(s, k + 1, j, 0, dp)
        
                if s[k] == '&':
                    temp_ans += lt * rt if isTrue == 1 else lt * rf + lf * rt + lf * rf
                elif s[k] == '|':
                    temp_ans += lt * rt + lt * rf + lf * rt if isTrue == 1 else lf * rf
                elif s[k] == '^':
                    temp_ans += lt * rf + lf * rt if isTrue == 1 else lt * rt + lf * rf
        
            dp[i][j][isTrue] = temp_ans
            return dp[i][j][isTrue]
        dp = [[[-1 for _ in range(2)] for _ in range(n)] for _ in range(n)]
        return solve(s, 0, n - 1, 1, dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input().strip()
        print(Solution().countWays(s))
        print("~")

# } Driver Code Ends