class Solution:
	def pythagoreanTriplet(self, arr):
    	# code here
        arr=list(set(arr))
        n=len(arr)
        for i in range(n):
            arr[i]=arr[i]*arr[i]
        for i in range(n):
            for j in range(i-1,-1,-1):
                if arr[i]+arr[j] in arr:
                    return True
        return False