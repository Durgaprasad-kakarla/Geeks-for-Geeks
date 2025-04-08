class Solution:
    def isBridge(self, V, edges, c, d):
        # code here 
        def dfs(node,vis):
            vis[node]=1
            for i in adj[node]:
                if not vis[i]:
                    dfs(i,vis)
        adj=[[] for _ in range(V)]
        vis=[0 for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        cnt=0
        for i in range(V):
            if not vis[i]:
                dfs(i,vis)
                cnt+=1
        adj=[[] for _ in range(V)]
        vis=[0 for _ in range(V)]
        for u,v in edges:
            if (u==c and v==d) or (u==d and v==c):
                continue
            adj[u].append(v)
            adj[v].append(u)
        cnt1=0
        for i in range(V):
            if not vis[i]:
                dfs(i,vis)
                cnt1+=1
        return cnt1>cnt
        


#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        adj = [[] for _ in range(V)]
        edges = []

        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)
            edges.append([u, v])

        c = int(input())
        d = int(input())

        obj = Solution()
        l = obj.isBridge(V, edges, c, d)

        if l:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends