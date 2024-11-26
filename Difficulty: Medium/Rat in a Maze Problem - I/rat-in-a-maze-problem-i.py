#User function Template for python3
class Solution:
    # Function to find all possible paths
    def findPath(self, mat):
        # code here
        if mat[0][0]==0:
            return []
        def dfs(row,col,vis,s):
            if row==n-1 and col==m-1:
                ans.append(s)
                return 
            vis[row][col]=1
            dr=[-1,0,1,0]
            dc=[0,-1,0,1]
            dir={0:'U',1:'L',2:'D',3:'R'}
            for i in range(4):
                nrow=row+dr[i]
                ncol=col+dc[i]
                if nrow>=0 and ncol>=0 and nrow<n and ncol<m and not vis[nrow][ncol] and mat[nrow][ncol]==1:
                    dfs(nrow,ncol,vis,s+dir[i])
            vis[row][col]=0
        ans=[]
        n,m=len(mat),len(mat[0])
        vis=[[0 for i in range(m)] for j in range(n)]
        dfs(0,0,vis,'')
        return sorted(ans)
        
        




#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        input_line = input().strip()
        mat = eval(input_line)

        solution = Solution()
        result = solution.findPath(mat)

        if not result:
            print("[]")
        else:
            print(" ".join(result))
        print("~")

# } Driver Code Ends