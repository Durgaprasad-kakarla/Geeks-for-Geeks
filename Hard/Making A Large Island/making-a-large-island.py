from typing import List

class Solution:
    hm={}
    def largestIsland(self, grid : List[List[int]]) -> int:
        n = len(grid)
        name = 2
        vis = [[False for _ in range(n)] for _ in range(n)]

        def dfs(i, j, name):
            if i < 0 or j < 0 or i >= n or j >= n or grid[i][j] == 0 or vis[i][j]:
                return 0
            vis[i][j] = True
            grid[i][j] = name
            count = 1 + dfs(i + 1, j, name) + dfs(i - 1, j, name) + dfs(i, j - 1, name) + dfs(i, j + 1, name)
            return count

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1 and not vis[i][j]:
                    count = dfs(i, j, name)
                    self.hm[name] = count
                    name += 1

        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    d = grid[i + 1][j] if i + 1 < n else 0
                    u = grid[i - 1][j] if i - 1 >= 0 else 0
                    r = grid[i][j + 1] if j + 1 < n else 0
                    l = grid[i][j - 1] if j - 1 >= 0 else 0

                    s = {d, u, r, l}
                    res = 1
                    for val in s:
                        res += self.hm.get(val, 0)
                    ans = max(ans, res)

        if ans == 0:
            return n * n
        return ans
        




#{ 
 # Driver Code Starts

class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        grid=IntMatrix().Input(n,n)
        
        obj = Solution()
        res = obj.largestIsland(grid)
        
        print(res)
# } Driver Code Ends