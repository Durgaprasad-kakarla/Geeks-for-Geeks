class Solution:
	def maxSubstring(self, s):
		# code here
		n=len(s)
		cnt=0
		maxi=-float('inf')
		mini=float('inf')
		for i in range(n):
		    if s[i]=='1':
		        cnt-=1
		    else:
		        cnt+=1
		        maxi=max(maxi,cnt)
		        if i>0:
		            maxi=max(maxi,cnt-mini)
		  #  print(cnt,maxi,mini)
		    mini=min(mini,cnt)
		return maxi if maxi!=-float('inf') else -1