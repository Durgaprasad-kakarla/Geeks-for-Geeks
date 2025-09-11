class Solution:
	def minJumps(self, arr):
	    # code here
	    n=len(arr)
	    i,cnt=0,1
	    while i<n:
	        maxi,max_ind=-float('inf'),-1
	        if i+arr[i]>=n-1:
	            return 1
	        for j in range(i+1,i+arr[i]+1):
	            if maxi<(j+arr[j]):
	                maxi=j+arr[j]
	                max_ind=j
	       # print(max_ind,maxi,cnt)
	        if maxi>=n-1:
	            return cnt+1
	        if max_ind==-1:
	            return -1
	        i=max_ind
	        cnt+=1
	    return cnt