#User function Template for python3
class Solution:
	def minDifference(self, arr):
		# code here
		n=len(arr)
		target=sum(arr)
		dp=[[False for _ in range(target+1)] for _ in range(n)]
	    for i in range(target+1):
	        if i==arr[0]:
	            dp[0][i]=True
	    for i in range(1,n):
	        for j in range(target+1):
	            l=False
	            if j>=arr[i]:
	                l=dp[i-1][j-arr[i]]
	            r=dp[i-1][j]
	            dp[i][j]=l or r
	   # print(dp[-1])
	    mini=float('inf')
	    for i in range(target+1):
	        if dp[n-1][i]==True:
	            mini=min(mini,abs((target-i)-i))
	    return mini