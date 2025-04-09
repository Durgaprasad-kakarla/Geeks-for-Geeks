class Solution:
    def articulationPoints(self, n, connections):
        # code here
        global timer
        timer=0
        def dfs(node, parent, vis, tin, low, mark, adj):
            global timer
            vis[node] = True
            tin[node] = low[node] = timer
            timer += 1
            child = 0
    
            for it in adj[node]:
                if it == parent:
                    continue
                if not vis[it]:
                    dfs(it, node, vis, tin, low, mark, adj)
                    low[node] = min(low[node], low[it])
                    if low[it] >= tin[node] and parent != -1:
                        mark[node] = True
                    child += 1
                else:
                    low[node] = min(low[node], tin[it])
            
            if parent == -1 and child > 1:
                mark[node] = True
        adj=[[] for i in range(n)]
        for u,v in connections:
            adj[u].append(v)
            adj[v].append(u)
        vis = [False] * n
        tin = [0] * n
        low = [0] * n
        mark = [False] * n

        for i in range(n):
            if not vis[i]:
                dfs(i, -1, vis, tin, low, mark, adj)

        ans = [i for i in range(n) if mark[i]]
        return ans if ans else [-1]


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(int(1e7))


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append([u, v])
        obj = Solution()
        ans = obj.articulationPoints(V, edges)
        ans.sort()
        print(" ".join(map(str, ans)))
        print("~")


if __name__ == "__main__":
    main()
# } Driver Code Ends