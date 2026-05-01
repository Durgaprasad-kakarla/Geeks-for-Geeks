import heapq
class Solution:
    def kthLargest(self, arr, k):
        # code here 
        n=len(arr)
        heap=[]
        ans=[]
        for i in range(n):
            if i<k-1:
                heapq.heappush(heap,arr[i])
                ans.append(-1)
            elif i==k-1:
                heapq.heappush(heap,arr[i])
                ans.append(heap[0])
            else:
                if len(heap)==k and heap[0]*1<arr[i]:
                    heapq.heappop(heap)
                    heapq.heappush(heap,1*arr[i])
                ans.append(heap[0])
            # print(heap)
        return ans
            