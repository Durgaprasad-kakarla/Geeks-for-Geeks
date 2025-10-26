import heapq
class Solution:
   def minCost(self, arr):
    # code here
    heap=[]
    for i in arr:
        heapq.heappush(heap,i)
    cost=0
    while len(heap)>1:
        ele1=heapq.heappop(heap)
        ele2=heapq.heappop(heap)
        cost+=(ele1+ele2)
        heapq.heappush(heap,ele1+ele2)
    return cost