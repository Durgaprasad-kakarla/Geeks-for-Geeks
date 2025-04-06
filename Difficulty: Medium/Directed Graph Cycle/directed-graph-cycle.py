
class Solution:
    def isCycle(self, V, edges):
        # code here
        def dfs(node):
            vis[node]=1
            pathvis[node]=1
            for i in adj[node]:
                if not vis[i]:
                    if dfs(i):
                        return True
                elif pathvis[i]==1:
                    return True
            pathvis[node]=0
            return False
        adj=[[] for i in range(V)]
        vis,pathvis=[0 for i in range(V)],[0 for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
        for i in range(V):
            if not vis[i] and dfs(i):
                return True
        return False
        

#{ 
 # Driver Code Starts
from collections import deque


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))

        obj = Solution()
        ans = obj.isCycle(V, edges)
        print("true" if ans else "false")


if __name__ == "__main__":
    main()

# } Driver Code Ends