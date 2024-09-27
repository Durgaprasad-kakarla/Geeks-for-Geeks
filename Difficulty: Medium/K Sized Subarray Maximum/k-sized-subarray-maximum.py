#User function Template for python3

class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,k,arr):
        queue,ans=[],[]
        n=len(arr)
        for i in range(n):
            if queue!=[] and queue[0]==i-k:
                queue.pop(0)
            while queue and arr[queue[-1]]<arr[i]:
                queue.pop()
            queue.append(i)
            if i>=k-1:
                ans.append(arr[queue[0]])
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
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.max_of_subarrays(k, arr)
        for i in range(len(res)):
            print(res[i], end=" ")
        print()

# } Driver Code Ends