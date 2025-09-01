from heapq import heappush,heappop
from collections import defaultdict
class Solution:
    def sumOfModes(self, arr, k):
        # code here
        n=len(arr)
        heap=[]
        dic=defaultdict(int)
        ans=0
        for j in range(n):
            dic[arr[j]]+=1
            if j>=k:
                dic[arr[j-k]]-=1
            heappush(heap,(-dic[arr[j]],arr[j]))
            
            while dic[heap[0][1]]!=-heap[0][0]:
                heappop(heap)
            if j>=k-1:
                ans+=heap[0][1]
        return ans
            
        
