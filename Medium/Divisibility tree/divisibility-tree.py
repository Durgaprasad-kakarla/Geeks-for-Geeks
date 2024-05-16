
from typing import List

class Solution:
    def minimumEdgeRemove(self, n : int, edges : List[List[int]]) -> int:
        global min_edges
        min_edges=0
        def dfs(node):
            global min_edges
            vis[node]=1
            cnt=0
            for i in adj[node]:
                if not vis[i]:
                    cnt+=dfs(i)
            if cnt+1&1==0:
                min_edges+=1
            return cnt+1
        adj=[[] for i in range(n)]
        vis=[0 for i in range(n)]
        for u,v in edges:
            adj[u-1].append(v-1)
            adj[v-1].append(u-1)
        dfs(0)
        return min_edges-1
        



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        edges = IntMatrix().Input(n - 1, 2)

        obj = Solution()
        res = obj.minimumEdgeRemove(n, edges)

        print(res)

# } Driver Code Ends