#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

#User function Template for python3

class Solution:
    def longestStringChain(self, words):
        # Code here
        dp = {}
        res = 1
        for word in sorted(words, key=len):
            dp[word] = 1
            for i in range(len(word)):
                prev = word[:i] + word[i + 1 :]
                if prev in dp:
                    dp[word] = max(dp[word], dp[prev] + 1)
                    res = max(res, dp[word])
        return res

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input())
    for _ in range (t):
        words = input().split()
        ob = Solution()
        res = ob.longestStringChain(words)
        print(res)
        print("~")
# } Driver Code Ends