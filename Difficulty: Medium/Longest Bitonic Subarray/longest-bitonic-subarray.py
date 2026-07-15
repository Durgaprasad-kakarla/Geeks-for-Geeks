class Solution:
	def bitonic(self,arr):
		# code here
		n=len(arr)
		pref=[0]*n
		pref[0]=1
		for i in range(1,n):
		    if arr[i-1]<=arr[i]:
		        pref[i]+=pref[i-1]+1
		    else:
		        pref[i]=1
		curr=1
		maxi=max(pref)
		for i in range(n-2,-1,-1):
		    if arr[i]>=arr[i+1]:
		        curr+=1
		    else:
		        curr=1
		    maxi=max(maxi,curr,pref[i]+curr-1)
		return maxi