#User function Template for python3

class Solution:
	def distinctSubsequences(self, s):
		# code here
        n=len(s)
        dp=[0]*(n+1)
        dic={}
        dp[0]=1
        i=1
        while i<(n+1):
            dp[i]=(dp[i-1]*2)%(10**9+7)
            c=s[i-1]
            if c in dic:
                dp[i]-=dp[dic[c]-1]
            dic[c]=i
            i+=1
        return dp[i-1]%(10**9+7)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()

		ob = Solution()
		answer = ob.distinctSubsequences(s)
		print(answer)

# } Driver Code Ends