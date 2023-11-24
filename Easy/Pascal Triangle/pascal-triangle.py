#User function Template for python3

#User function Template for python3
class Solution:

	def nthRowOfPascalTriangle(self,n):
	    # code here
        if n == 0:
            return [1]

        row = [1]

        for i in range(1, n ):
            new_row = [1] * (i + 1)
            for j in range(1, i):
                new_row[j] = (row[j - 1] + row[j]) % (10**9 + 7)
            row = new_row

        return row

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    ob = Solution()
	    ans=ob.nthRowOfPascalTriangle(n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends