class Solution:
	def pushZerosToEnd(self, arr):
    	# code here
    	n=len(arr)
    	l,r=0,0
    	while r<n:
    	    if arr[l]>0:
    	        if arr[r]>0:
    	            l+=1
    	        r+=1
    	    else:
    	        if arr[r]>0:
        	        arr[l],arr[r]=arr[r],arr[l]
        	        l+=1
        	    r+=1
    	return arr
    	        