#User function Template for python3
class Solution:

	def countStrings(self,n):
    	# code here
        if n==1:
            return 2
        if n==2:
            return 3
        a,b=2,3
        for i in range(n-2):
            c=(a+b)%(10**9+7)
            a=b
            b=c
        return b%(10**9+7)

#{ 
 # Driver Code Starts
#Initial Template for Python 3



# Driver code 
if __name__ == "__main__": 		
    tc=int(input())
    while tc > 0:
        n=int(input())
        ob = Solution()
        ans = ob.countStrings( n)
        print(ans)
        tc=tc-1
# } Driver Code Ends