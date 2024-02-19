#User function Template for python3

class Solution:
    def wordBreak(self, s, wordDict):
        # Complete this function
        wordset=set(wordDict)
        if s in wordset:
            return 1
        dp={}
        def dfs(s):
            if s in dp:
                return dp[s]
            for i in range(1,len(s)):
                prefix=s[:i]
                suffix=s[i:]
                if (prefix in wordset and suffix in wordset) or (prefix in wordset and dfs(suffix)):
                    dp[s]=True
                    return dp[s]
            dp[s]=False
            return dp[s]
        if dfs(s):
            return 1
        else:
            return 0

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		number_of_elements = int(input())
		dictionary = [word for word in input().strip().split()]
		line = input().strip()
		ob = Solution()
		res = ob.wordBreak(line, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends