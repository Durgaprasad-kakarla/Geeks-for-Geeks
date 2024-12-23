#User function Template for python3
import heapq

class Solution:

    def kthSmallest(self, arr,k):
        heap=[]
        for i in arr:
            heapq.heappush(heap,i)
        while heap and k>1:
            heapq.heappop(heap)
            k-=1
        return heapq.heappop(heap)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    import random
    t = int(input())
    for tcs in range(t):
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.kthSmallest(arr, k))
        print("~")
# } Driver Code Ends