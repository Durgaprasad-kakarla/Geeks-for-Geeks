#User function Template for python3

class Solution:
    
     #Function to count number of pairs such that x^y is greater than y^x.     
    def countPairs(self,arr,brr):
        #code here
        n,m=len(arr),len(brr)
        for i in range(n):
            arr[i]=pow(arr[i],1/arr[i])
        for i in range(m):
            brr[i]=pow(brr[i],1/brr[i])
        brr.sort(reverse=True)
        arr.sort(reverse=True)
        i,j=0,0
        tot=0
        while i<n and j<m:
            if arr[i]>brr[j]:
                tot+=(m-j)
                i+=1
            else:
                j+=1
        return tot


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3

import atexit
import io
import sys
import bisect

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        # M, N = map(int, input().strip().split())
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.countPairs(a, b))
        #code here

# } Driver Code Ends