#User function Template for python3
from typing import List
import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr: List[int]) -> int:
        heap=[]
        n=len(arr)
        for i in range(n):
            heapq.heappush(heap,arr[i])
        total=0
        while len(heap)>1:
            ele1=heapq.heappop(heap)
            ele2=heapq.heappop(heap)
            sm=ele1+ele2
            total+=sm
            heapq.heappush(heap,sm)
        return total

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
import heapq
from collections import defaultdict
# Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minCost(a))

# } Driver Code Ends