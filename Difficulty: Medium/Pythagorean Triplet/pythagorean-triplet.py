class Solution:
	def pythagoreanTriplet(self, arr):
    	# code here
    	arr=list(set(arr))
    	arr=[i*i for i in arr]
    	n=len(arr)
    	for i in range(n):
    	    for j in range(i+1,n):
    	        if arr[i]+arr[j] in arr:
    	            return True
    	return False