class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        queue=deque()
        n=len(arr)
        ans=[]
        for i in range(n):
            while queue and queue[-1][0]<=arr[i]:
                queue.pop()
            queue.append([arr[i],i])
            while queue and i-queue[0][1]>=k:
                queue.popleft()
            if i-k+1>=0:
                ans.append(queue[0][0])
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

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
        arr = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        res = ob.maxOfSubarrays(arr, k)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()
        print("~")
# } Driver Code Ends