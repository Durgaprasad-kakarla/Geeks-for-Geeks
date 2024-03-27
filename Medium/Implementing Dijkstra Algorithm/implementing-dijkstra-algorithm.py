import heapq
class Solution:

    #Function to find the shortest distance of all the vertices
    #from the source vertex S.
    def dijkstra(self, vertices, adj, source):
        #code here
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
#Initial Template for Python 3
import atexit
import io
import sys


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V,E = map(int,input().strip().split())
        adj = [[] for i in range(V)]
        for i in range(E):
            u,v,w = map(int,input().strip().split())
            adj[u].append([v,w])
            adj[v].append([u,w])
        S=int(input())
        ob = Solution()
        
        res = ob.dijkstra(V,adj,S)
        for i in res:
            print(i,end=" ")
        print()
# } Driver Code Ends