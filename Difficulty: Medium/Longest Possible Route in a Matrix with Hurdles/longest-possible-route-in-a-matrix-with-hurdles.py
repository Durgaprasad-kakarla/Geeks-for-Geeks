import heapq
class Solution:
    def longestPath(self, mat, xs, ys, xd, yd):
        # code here
        n,m=len(mat),len(mat[0])
        def dfs(row,col):
            if row==xd and col==yd:
                return 0
            vis[row][col]=1
            dr=[-1,0,1,0]
            dc=[0,-1,0,1]
            ans=-1
            for i in range(4):
                nrow=row+dr[i]
                ncol=col+dc[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and not vis[nrow][ncol] and mat[nrow][ncol]==1:
                    cur=dfs(nrow,ncol)
                    if cur!=-1:
                        ans=max(ans,cur+1)
            vis[row][col]=0
            return ans
        vis=[[0 for _ in range(m)] for _ in range(n)]
        if mat[xs][ys]==0 or mat[xd][yd]==0:
            return -1
        return dfs(xs,ys)