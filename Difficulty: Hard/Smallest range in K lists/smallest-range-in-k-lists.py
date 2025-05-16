import heapq
class Solution:
    def findSmallestRange(self, arr):
        # code here
        n,k=len(arr),len(arr[0])
        max_val=-float('inf')
        heap=[]
        for i in range(n):
            heapq.heappush(heap,[arr[i][0],i,0])
            max_val=max(max_val,arr[i][0])
        best=[-float('inf'),float('inf')]
        while True:
            min_val,row,ind=heapq.heappop(heap)
            if best[1]-best[0]>max_val-min_val:
                best=[min_val,max_val]
            if ind+1>=len(arr[row]):
                break
            heapq.heappush(heap,[arr[row][ind+1],row,ind+1])
            max_val=max(max_val,arr[row][ind+1])
        return best
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