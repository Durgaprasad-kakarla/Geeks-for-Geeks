#User function Template for python3
class Solution:
	def matSearch(self, mat, x):
		# Complete this function
		n,m=len(mat),len(mat[0])
		l,r,ans=0,n-1,-1
		for i in range(n):
		    if mat[i][0]<=x and mat[i][m-1]>=x:
        		l,r=0,m-1
        		while l<=r:
        		    mid=(l+r)//2
        		    if mat[i][mid]<x:
        		        l=mid+1
        		    elif mat[i][mid]>x:
        		        r=mid-1
        		    else:
        		        return True
        return False


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c
        x = int(data[index])
        index += 1
        ob = Solution()
        if ob.matSearch(matrix, x):
            print("true")
        else:
            print("false")
        print("~")
# } Driver Code Ends