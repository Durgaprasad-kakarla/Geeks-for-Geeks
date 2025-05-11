from typing import List
import heapq

class Solution:
    def kthLargest(self, arr, k) -> int:
        # code here
        n=len(arr)
        heap=[]
        for i in range(n):
            sm=0
            for j in range(i,n):
                sm+=arr[j]
                if heap and len(heap)>=k and heap[0]<=sm:
                    heapq.heappop(heap)
                    heapq.heappush(heap,sm)
                if len(heap)<k:
                    heapq.heappush(heap,sm)
        return heap[0]
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

# Position this line where user code will be pasted.

#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.kthLargest(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends