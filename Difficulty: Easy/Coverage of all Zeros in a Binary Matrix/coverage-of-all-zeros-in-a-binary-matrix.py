#User function Template for python3

class Solution:
	def findCoverage(self, matrix):
		# Code here
        def find_count(row,col,matrix):
            n,m=len(matrix),len(matrix[0])
            dr=[-1,0,1,0]
            dc=[0,1,0,-1]
            cnt=0
            for i in range(4):
                nrow=row+dr[i]
                ncol=col+dc[i]
                if nrow>=0 and ncol>=0 and nrow<n and ncol<m and matrix[nrow][ncol]==1:
                    cnt+=1
            return cnt
        n,m=len(matrix),len(matrix[0])
        tot=0
        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    tot+=(find_count(i,j,matrix))
        return tot

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n, m = input().split()
        n = int(n)
        m = int(m)
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        ob = Solution()
        ans = ob.findCoverage(matrix)
        print(ans)

# } Driver Code Ends