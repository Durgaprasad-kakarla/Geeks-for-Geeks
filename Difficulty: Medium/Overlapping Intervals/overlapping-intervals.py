class Solution:
	def mergeOverlap(self, arr):
		# Code here
		arr.sort()
		n=len(arr)
		ans=[arr[0]]
		for i in range(1,n):
		    start,end=arr[i]
		    if ans[-1][1]>=start:
		        ans[-1][1]=max(ans[-1][1],end)
		        ans[-1][0]=min(ans[-1][0],start)
		    else:
		        ans.append(arr[i])
		return ans