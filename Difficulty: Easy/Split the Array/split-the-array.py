#User function Template for python3
class Solution:
	def countgroup(self,arr): 
		#Complete the function
		xor=0
		n=len(arr)
	    for i in range(n):
	        xor^=arr[i]
	    if xor==0:
	        return (2**(n-1)-1)%(10**9+7)
        else:
            return 0


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.countgroup(arr)
        print(res)
        t -= 1

# } Driver Code Ends