#User function Template for python3
class Solution:
	def NBitBinary(self, n):
		# code here
		final=[]
        def func(n,cnt1,cnt0,s,final):
            if n==0:
                final.append(s)
                return 
            func(n-1,cnt1+1,cnt0,s+'1',final)
            if cnt1>cnt0:
                func(n-1,cnt1,cnt0+1,s+'0',final)
        func(n,0,0,'',final)
        return (final)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		ob = Solution()	
		answer = ob.NBitBinary(n)
		for value in answer:
			print(value,end=" ")
		print()


# } Driver Code Ends