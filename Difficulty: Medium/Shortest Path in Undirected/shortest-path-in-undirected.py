from collections import deque
class Solution:
    def shortestPath(self, adj, src):
        # code her
        n=len(adj)
        dist=[float('inf')]*n
        dist[src]=0
        queue=deque()
        queue.append([src,0])
        while queue:
            node,d=queue.popleft()
            for i in adj[node]:
                if dist[i]>dist[node]+1:
                    dist[i]=dist[node]+1
                    queue.append([i,dist[i]])
        for i in range(n):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist


#{ 
 # Driver Code Starts
# Initial Template for Python 3
from collections import deque

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        V = int(input())
        E = int(input())
        adj = [[] for _ in range(V)]

        for _ in range(E):
            u, v = map(int, input().split())
            adj[u].append(v)
            adj[v].append(u)  # Since the graph is undirected

        src = int(input())

        ob = Solution()
        ans = ob.shortestPath(adj, src)

        print(" ".join(map(str, ans)))
        print("~")
        tc -= 1

# } Driver Code Ends