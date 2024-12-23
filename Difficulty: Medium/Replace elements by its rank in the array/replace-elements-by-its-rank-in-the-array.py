#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
import heapq
class Solution:
    def replaceWithRank(self, n, arr):
        # Code here
        rank=1
        heap=[]
        for i in range(n):
            heapq.heappush(heap,[arr[i],i])
        prev=-1
        rank_arr=[0]*n
        while heap:
            ele,ind=heapq.heappop(heap)
            if prev!=-1 and prev==ele:
                rank_arr[ind]=rank-1
            else:
                rank_arr[ind]=rank
                rank+=1
            prev=ele
        return rank_arr

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.replaceWithRank(N, arr)
        for rank in res:
            print(rank, end = ' ')
        print()
        print("~")
# } Driver Code Ends