#User function Template for python3
class Solution:
	def minJumps(self, arr):
	    #code here
	    n=len(arr)
	    i=1
	    start=arr[0]
	    if start==0:
	        return -1
	    if start>=n-1:
	        return 1
	    jumps=0
	    while i<n:
	        maxi,index=-float('inf'),-1
	        while start>0 and i<n:
	            if maxi<(i+arr[i]):
	                maxi=i+arr[i]
	                index=i
	            i+=1
	            start-=1
	        jumps+=1
	        if index==-1:
	            return -1
	        if maxi>=n-1:
	            return jumps+1
            start=arr[index]
            i=index+1
	    return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        # n = int(input())
        Arr = [int(x) for x in input().split()]
        ob = Solution()
        ans = ob.minJumps(Arr)
        print(ans)

# } Driver Code Ends