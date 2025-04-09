class Solution:
    
    def topoSort(self, V, edges):
        # Code here
        def dfs(node):
            vis[node]=1
            for i in adj[node]:
                if not vis[i]:
                    dfs(i)
            topo.append(node)
        vis=[0 for _ in range(V)]
        adj=[[] for i in range(V)]
        for u,v in edges:
            adj[u].append(v)
        topo=[]
        for i in range(V):
            if not vis[i]:
                dfs(i)
        return topo[::-1]


#{ 
 # Driver Code Starts
# Driver Program

import sys

sys.setrecursionlimit(10**6)


def check(graph, N, res):
    if N != len(res):
        return False
    map = [0] * N
    for i in range(N):
        map[res[i]] = i
    for i in range(N):
        for v in graph[i]:
            if map[i] > map[v]:
                return False
    return True


def main():
    tc = int(input())
    for _ in range(tc):
        V = int(input())
        E = int(input())
        x = V
        edges = []
        adj = [[] for i in range(V)]
        for _ in range(E):
            u, v = map(int, input().split())
            edges.append((u, v))
            adj[u].append(v)

        obj = Solution()
        res = obj.topoSort(V, edges)

        if check(adj, x, res):
            print("true")
        else:
            print("false")
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends