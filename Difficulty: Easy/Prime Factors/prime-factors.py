#User function Template for python3

class Solution:
	def AllPrimeFactors(self, n):
		# Code here
	    if n==1:
	        return []
		if n<4:
		    return [n]
		i=2
		ans=[]
		while i*i<=n:
		    flag=1
		    while n%i==0:
		        flag=0
		        n//=i
		    if flag==0:
		        ans.append(i)
		    i+=1
		if n>=2:
		    ans.append(n)
		return ans
		    
		        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		ob = Solution()
		ans = ob.AllPrimeFactors(N)
		for _ in ans:
			print(_, end = " ")
		print()
# } Driver Code Ends