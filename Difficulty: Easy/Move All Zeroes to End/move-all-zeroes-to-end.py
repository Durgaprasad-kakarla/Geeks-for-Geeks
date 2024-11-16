#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	n=len(arr)
    	l,r=0,0
    	while r<n:
    	    if arr[l]==0:
    	        if arr[r]==0:
    	            r+=1
    	        else:
    	            arr[l],arr[r]=arr[r],arr[l]
    	            r+=1
    	            l+=1
    	    else:
	            l+=1
	            r+=1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.pushZerosToEnd(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1
# } Driver Code Ends