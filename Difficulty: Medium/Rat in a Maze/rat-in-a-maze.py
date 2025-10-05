class Solution:
    def ratInMaze(self, maze):
        # code here
        n,m=len(maze),len(maze[0])
        def rat_in_maze(row,col,s):
            if row<0 or row>=n or col<0 or col>=m:
                return 
            if row==n-1 and col==m-1:
                ans.append(s)
                return 
            if maze[row][col]==1 and not vis[row][col]:
                vis[row][col]=1
                rat_in_maze(row-1,col,s+'U')
                rat_in_maze(row+1,col,s+'D')
                rat_in_maze(row,col-1,s+'L')
                rat_in_maze(row,col+1,s+'R')
                vis[row][col]=0
        ans=[]
        vis=[[0 for i in range(m)] for j in range(n)]
        rat_in_maze(0,0,'')
        return sorted(ans)