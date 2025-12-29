import heapq
class Solution:
    def kthElement(self, a, b, k):
        # code here
        n,m=len(a),len(b)
        heap=[]
        heapq.heappush(heap,[a[0],0,'a'])
        heapq.heappush(heap,[b[0],0,'b'])
        while heap and k>0:
            ele,ind,arr=heapq.heappop(heap)
            k-=1
            if arr=='a':
                if ind+1<n:
                    heapq.heappush(heap,[a[ind+1],ind+1,arr])
            else:
                if ind+1<m:
                    heapq.heappush(heap,[b[ind+1],ind+1,arr])
        return ele