#User function Template for python3

class Solution:
	def is_bleak(self, n):
		# Code here
        def count_bits(n):
            res=0
            while n>0:
                n=(n&(n-1))
                res+=1
            return res
        for i in range(n-32,n+1):
            if i+count_bits(i)==n:
                return 0
        return 1
        ''' Time Complexity--O(logn*logn)
            Space Complexity--O(1)'''

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution();
		ans = ob.is_bleak(n)
		print(ans)

# } Driver Code Ends