class Solution:
	def maxSumIS(self, arr):
		# code here
		n=len(arr)
		dp=arr.copy()
		for i in range(n):
		    maxi=0
		    for j in range(i-1,-1,-1):
		        if arr[i]>arr[j]:
		            maxi=max(maxi,dp[j])
		    dp[i]=maxi+dp[i]
		return max(dp)