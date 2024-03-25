#User function Template for python3

from typing import List
import heapq
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        heap=[]
        heapq.heappush(heap,[0,start])
        dist=[float('inf')]*100000
        dist[start]=0
        while heap:
            op,ele=heapq.heappop(heap)
            if ele==end:
                return op
            for i in arr:
                x=(i*ele)%100000
                if dist[x]>1+dist[ele]:
                    dist[x]=1+dist[ele]
                    heapq.heappush(heap,[dist[x],x])
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().strip().split()]
        start, end = list(map(int,input().split()))
        obj=Solution()
        print(obj.minimumMultiplications(arr, start, end))
# } Driver Code Ends