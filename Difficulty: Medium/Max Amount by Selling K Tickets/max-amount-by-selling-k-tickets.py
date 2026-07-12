import heapq
class Solution:
    def maxAmount(self, arr, k):
        # code here
        heap=[]
        for i in arr:
            heapq.heappush(heap,-i)
        tot=0
        while heap and k>0:
            ele=heapq.heappop(heap)
            ele*=-1
            if ele<=0:
                continue
            k-=1
            tot=(tot+ele)%(10**9+7)
            heapq.heappush(heap,-(ele-1))
        return tot%(10**9+7)