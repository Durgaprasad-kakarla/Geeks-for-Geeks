#User function Template for python3
class Solution:

	def nthRowOfPascalTriangle(self, n):
	    # code here
	    def ncr(n,r):
	        ans=1
	        for i in range(r):
	            ans=((ans*n)//(i+1))
	            n-=1
	        return ans
	    lst=[]
	    for i in range(n):
	        lst.append(ncr(n-1,i))
	    return lst

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.nthRowOfPascalTriangle(n)
        for x in ans:
            print(x, end=" ")
        print()
        tc = tc - 1
        print("~")
# } Driver Code Ends