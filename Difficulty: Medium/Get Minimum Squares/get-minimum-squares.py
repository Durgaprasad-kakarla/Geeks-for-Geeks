import math
class Solution:
	def minSquares(self, n):
		# Code here
		def min_squares(n):
		    if n<=0:
		        return 0
		    if dp[n]!=-1:
		        return dp[n]
		    sqrt=int(math.sqrt(n))+1
		    mini=float('inf')
		    for i in range(sqrt-1,0,-1):
		        mini=min(mini,1+min_squares(n-i*i))
		    dp[n]=mini
		    return mini
		dp=[-1 for i in range(n+1)]
		return min_squares(n)
		