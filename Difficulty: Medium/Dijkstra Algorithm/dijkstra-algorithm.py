import heapq
class Solution:
    # Returns shortest distances from src to all other vertices
    def dijkstra(self, vertices, edges, source):
        # code here
        adj=[[] for _ in range(vertices)]
        for u,v,wt in edges:
            adj[u].append([v,wt])
        heap=[]
        heapq.heappush(heap,[source,0])
        dist=[float('inf')]*(vertices)
        dist[source]=0
        while heap:
            node,d=heapq.heappop(heap)
            for u,wt in adj[node]:
                if dist[node]+wt<dist[u]:
                    dist[u]=dist[node]+wt
                    heapq.heappush(heap,[u,dist[u]])
        return dist


#{ 
 # Driver Code Starts
# Initial Template for Python 3
import sys
import heapq

# Position this line where user code will be pasted.


def main():
    t = int(input())
    for _ in range(t):
        V = int(input())
        E = int(input())
        edges = []
        for _ in range(E):
            u, v, w = map(int, input().split())
            edges.append([u, v, w])
            edges.append([v, u, w])  # Since the graph is undirected

        src = int(input())

        obj = Solution()
        res = obj.dijkstra(V, edges, src)

        print(" ".join(map(str, res)))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends