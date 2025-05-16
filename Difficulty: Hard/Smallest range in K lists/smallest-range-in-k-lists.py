import heapq
class Solution:
    def findSmallestRange(self, arr):
        # code here
        n = len(arr)
        k = len(arr[0])
    
        heap = []
        max_val = float('-inf')
    
        for i in range(n):
            val = arr[i][0]
            heapq.heappush(heap, (val, i, 0))
            max_val = max(max_val, val)
    
        best_range = [float('-inf'), float('inf')]
    
        while True:
            min_val, row, idx = heapq.heappop(heap)
            if max_val - min_val < best_range[1] - best_range[0]:
                best_range = [min_val, max_val]
            if idx + 1 == len(arr[row]):
                break
            next_val = arr[row][idx + 1]
            heapq.heappush(heap, (next_val, row, idx + 1))
            max_val = max(max_val, next_val)
    
        return best_range

#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())
for _ in range(t):
    n = int(input())
    k = int(input())
    arr = []
    for _ in range(k):
        arr.append(list(map(int, input().strip().split())))
    r = Solution().findSmallestRange(arr)
    print(r[0], r[1])
    print("~")

# } Driver Code Ends