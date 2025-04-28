#User function Template for python3
import heapq
from typing import List
 
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        n=len(arr)
        dist=[float('inf')]*100000
        dist[start]=0
        heap=[]
        heapq.heappush(heap,[0,start])
        while heap:
            d,node=heapq.heappop(heap)
            if node==end:
                return d
            for i in arr:
                ele=(i*node)%100000
                if dist[ele]>d+1:
                    dist[ele]=d+1
                    heapq.heappush(heap,[d+1,ele])
        return dist[end] if dist[end]!=float('inf') else -1

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
        print("~")
# } Driver Code Ends