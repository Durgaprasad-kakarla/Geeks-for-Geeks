#User function Template for python3

class Solution:
	def nthStair(self,n):
		# Code here
		dp=[0]*(n+1)
		dp[0],dp[1]=0,1
		for i in range(2,n+1):
		    if i&1==0:
		        dp[i]=dp[i-1]+1
		    else:
		        dp[i]=dp[i-1]
		return dp[n]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.nthStair(n)
		print(ans)
# } Driver Code Ends