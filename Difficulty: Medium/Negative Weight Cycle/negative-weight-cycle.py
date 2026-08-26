class Solution:
    def isNegativeWeightCycle(self, V: int, edges: list[list[int]]) -> bool:
        # code here
        dist=[float('inf')]*V
        dist[0]=0
        for i in range(V-1):
            for u,v,wt in edges:
                if dist[v]>dist[u]+wt:
                    dist[v]=dist[u]+wt
        for u,v,wt in edges:
            if dist[v]>dist[u]+wt:
                return True
        return False