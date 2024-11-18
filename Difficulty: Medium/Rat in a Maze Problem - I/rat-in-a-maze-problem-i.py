from typing import List

class Solution:
    def findPath(self, mat: List[List[int]]) -> List[str]:
        # code here
        n,m=len(mat),len(mat[0])
        def dfs(row,col,vis,mat,s):
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
                    dfs(nrow,ncol,vis,mat,s+dir[i])
            vis[row][col]=0
        ans=[]
        vis=[[0 for i in range(m)] for j in range(n)]
        if mat[0][0]==0:
            return []
        dfs(0,0,vis,mat,"")
        return ans


#{ 
 # Driver Code Starts
# Main function to read input and output the results
if __name__ == "__main__":
    t = int(input().strip())
    for _ in range(t):
        n = int(input().strip())
        m = []
        for i in range(n):
            m.append(list(map(int, input().strip().split())))
        obj = Solution()
        result = obj.findPath(m)
        result.sort()
        if len(result) == 0:
            print(-1)
        else:
            print(" ".join(result))
        print("~")

# } Driver Code Ends