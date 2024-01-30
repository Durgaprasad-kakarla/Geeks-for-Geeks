#User function Template for python3

class Solution:
    def fill(self, n, m, mat):
        # code here
        m=len(mat)
        n=len(mat[0])
        vis=[[0 for i in range(n)] for j in range(m)]
        
        def dfs(row,col,vis):
            vis[row][col]=1
            dr=[0,-1,0,1]
            dc=[-1,0,1,0]
            for i in range(4):
                nrow=row+dr[i]
                ncol=col+dc[i]
                if nrow>=0 and nrow<m and ncol>=0 and ncol<n and not vis[nrow][ncol] and mat[nrow][ncol]=='O':
                    dfs(nrow,ncol,vis)
        for i in range(m):
            for j in range(n):
                if (i==0 or j==0 or i==m-1 or j==n-1) and not vis[i][j] and mat[i][j]=='O':
                    dfs(i,j,vis)
        for i in range(m):
            for j in range(n):
                if vis[i][j]==1:
                    mat[i][j]='O'
                else:
                    mat[i][j]='X'
        return mat

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, m = [int(x) for x in input().split()]
        mat = []
        for i in range(n):
            s = list(map(str,input().split()))
            mat.append(s)
        
        ob = Solution()
        ans = ob.fill(n, m, mat)
        for i in range(n):
            for j in range(m):
                print(ans[i][j], end = " ")
            print()
# } Driver Code Ends