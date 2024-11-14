#User function Template for python3
import heapq
class Solution:
    def nearlySorted(self, arr, k):
        #code
        n=len(arr)
        heap=[]
        for i in range(k+1):
            heapq.heappush(heap,arr[i])
        x=0
        for i in range(k+1,n):
            arr[x]=(heapq.heappop(heap))
            heapq.heappush(heap,arr[i])
            x+=1
        while heap:
            arr[x]=(heapq.heappop(heap))
            x+=1
        return arr
            

#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        ob.nearlySorted(arr, k)
        print(*arr)
        print("~")
        t -= 1
# } Driver Code Ends