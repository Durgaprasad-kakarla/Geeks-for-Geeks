#User function Template for python3

class Solution:
	def TotalWays(self, n):
		# Code here
		if n==1:
		    return 4
		if n==2:
		    return 9
		else:
            a,b=2,3
            for i in range(n-2):
                c=(a+b)%(10**9+7)
                a=b
                b=c
            return (b*b)%(10**9+7)

#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.TotalWays(N)
		print(ans)
# } Driver Code Ends