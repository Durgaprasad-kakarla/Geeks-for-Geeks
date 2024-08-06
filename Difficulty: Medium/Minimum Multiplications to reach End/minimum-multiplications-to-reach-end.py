#User function Template for python3

from typing import List
from collections import deque
class Solution:
    
    def minimumMultiplications(self, arr : List[int], start : int, end : int) -> int:
        # code here
        queue=deque()
        queue.append([0,start])
        dist=[float('inf')]*100000
        dist[start]=0
        while queue:
            # print(queue)
            d,node=queue.popleft()
            if node==end:
                return d
            for i in arr:
                mod=(node*i)%(100000)
                if dist[mod]>d+1:
                    dist[mod]=d+1
                    queue.append([dist[mod],mod])
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