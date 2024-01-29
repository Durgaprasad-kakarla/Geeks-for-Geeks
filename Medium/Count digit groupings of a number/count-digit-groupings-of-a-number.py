#User function Template for python3
from functools import lru_cache
class Solution:
	def TotalCount(self, s):
		# Code here
		n=len(s)
		def func(ind,prev,sm,dp):
		    if ind==n:
		        return 1
		    if dp[ind][prev+1]!=-1:
		        return dp[ind][prev+1]
		    tot=0
		    findsm=0
            for i in range(ind,n):
                findsm+=int(s[i])
                if prev==-1 or sm<=findsm:
                    tot+=func(i+1,ind,findsm,dp)
            dp[ind][prev+1]=tot
            return tot%(10**9+7)
        dp=[[-1 for i in range(n+1)] for j in range(n+1)]
        return func(0,-1,-1,dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.TotalCount(s)
		print(ans)
# } Driver Code Ends