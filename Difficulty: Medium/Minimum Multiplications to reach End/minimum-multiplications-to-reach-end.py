import heapq
class Solution:
    def minimumMultiplications(self, arr : list[int], start : int, end : int) -> int:
        # code here
        n=len(arr)
        mod=100000
        heap=[]
        heapq.heappush(heap,[0,start])
        dist=[float('inf')]*100001
        dist[start]=0
        while heap:
            d,node=heapq.heappop(heap)
            if node==end:
                return d
            for i in arr:
                curr=(node*i)%mod
                if dist[curr]>d+1:
                    dist[curr]=d+1
                    heapq.heappush(heap,[d+1,curr%mod])
        return -1