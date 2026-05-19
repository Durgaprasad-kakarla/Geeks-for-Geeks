import heapq
class Solution:
    def minSteps(self, arr, start, end):
        # code here2
        heap=[]
        mod=1000
        heapq.heappush(heap,[0,-start])
        dist=[float('inf')]*1000
        dist[start]=0
        while heap:
            d,node=heapq.heappop(heap)
            node*=-1
            node%=mod
            if node==end:
                return d
            for i in arr:
                curr=(node*i)%mod
                if dist[curr]>d+1:
                    dist[curr]=d+1
                    heapq.heappush(heap,[d+1,-curr])
        return -1