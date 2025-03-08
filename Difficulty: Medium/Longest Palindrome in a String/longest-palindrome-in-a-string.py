
class Solution:
    def longestPalindrome(self, s):
        # code here
        n=len(s)
        s1,s2=s,s[::-1]
        dp=[[0 for i in range(n+1)] for j in range(n+1)]
        max_len = 0
        end_index = 0
    
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]: 
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    original_index = i - dp[i][j] 
                    reversed_index = n - j 
                    if original_index == reversed_index:
                        if dp[i][j] > max_len:
                            max_len = dp[i][j]
                            end_index = i
        start_index = end_index - max_len
        return s[start_index:end_index]
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        ob = Solution()

        ans = ob.longestPalindrome(S)

        print(ans)
        print("~")
# } Driver Code Ends