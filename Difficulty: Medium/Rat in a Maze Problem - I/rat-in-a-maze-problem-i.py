from typing import List

class Solution:
    def findPath(self, mat: List[List[int]]) -> List[str]:
        # code here
        n,m=len(mat),len(mat[0])
        ans=[]
        def func(row,col,vis,s):
            if row==n-1 and col==m-1 and mat[row][col]==1:
                ans.append(s)
                return 
            if row<0 or row>=n or col<0 or col>=m or mat[row][col]==0 or vis[row][col]==1:
                return 
            vis[row][col]=1
            down=func(row+1,col,vis,s+'D')
            up=func(row-1,col,vis,s+'U')
            left=func(row,col-1,vis,s+'L')
            right=func(row,col+1,vis,s+'R')
            vis[row][col]=0
        vis=[[0 for i in range(m)] for j in range(n)]
        func(0,0,vis,'')
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

# } Driver Code Ends