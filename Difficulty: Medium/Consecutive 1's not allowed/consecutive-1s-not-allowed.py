class Solution:
	def countStrings(self,n):
    	# code here
    	dp=[0]*(n+1)
    	dp[1]=1
    	pref=[0]*(n+1)
    	pref[1]=1
    	tot=1
    	for i in range(2,n+1):
    	    dp[i]+=pref[i-2]+1
    	    pref[i]+=pref[i-1]+dp[i]
    	    tot+=dp[i]
    	return tot+1