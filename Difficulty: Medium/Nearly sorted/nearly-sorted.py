from heapq import heappush,heappop
class Solution:
    def nearlySorted(self, arr, k):  
        #code here
        heap=[]
        n=len(arr)
        for i in range(n):
            heappush(heap,arr[i])
        i=0
        while heap:
            arr[i]=heappop(heap)
            i+=1
        return arr