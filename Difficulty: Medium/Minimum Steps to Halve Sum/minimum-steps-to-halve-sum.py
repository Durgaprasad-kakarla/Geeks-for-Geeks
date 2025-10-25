import heapq
class Solution:
  def minOperations(self, arr):
    # code here
    tot=sum(arr)
    heap=[]
    for i in arr:
        heapq.heappush(heap,-i)
    half,cnt=tot,0
    while heap and half>tot/2:
        ele=-1*heapq.heappop(heap)
        half-=(ele/2)
        heapq.heappush(heap,-ele/2)
        cnt+=1
    return cnt