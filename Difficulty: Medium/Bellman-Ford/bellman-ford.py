#User function Template for python3
import sys
class Solution:
    def bellmanFord(self, V, edges, src):
        dist=[float('inf')]*V
        dist[src]=0
        for i in range(V-1):
            for u,v,wt in edges:
                if dist[v]>dist[u]+wt:
                    dist[v]=dist[u]+wt
        for u,v,wt in edges:
            if dist[v]>dist[u]+wt:
                return [-1]
        return [dist[i] if dist[i]!=float('inf') else 10**8 for i in range(V)]