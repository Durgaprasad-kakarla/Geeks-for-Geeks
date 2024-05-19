#User function Template for python3

class Solution:
	def PowMod(self, x, n, m):
		# Code here
		def power(n,x):
		    ans=1
		    base=n
		    while x>0:
		        if x%2==0:
		            base=(base*base)%m
		            x=x//2
		        else:
		            ans=(ans*base)%m
		            x-=1
		    return ans%m
		return power(x,n)%m
		            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		x, n , m = input().split()
		x = int(x)
		n = int(n) 
		m = int(m)
		ob = Solution();
		ans = ob.PowMod(x, n, m)
		print(ans)
# } Driver Code Ends