class Solution:
    #User function Template for python3
    #Function to count inversions in the array.
    def inversionCount(self, arr):
        # Your Code Here
        def merge(l,mid,r,arr):
            n=len(arr)
            low,high=l,mid+1
            tot=0
            while low<=mid:
                while high<=r and arr[low]>arr[high]:
                    high+=1
                tot+=high-(mid+1)
                low+=1
            lst=[]
            low,high=l,mid+1
            while low<=mid and high<=r:
                if arr[low]<=arr[high]:
                    lst.append(arr[low])
                    low+=1
                else:
                    lst.append(arr[high])
                    high+=1
            while low<=mid:
                lst.append(arr[low])
                low+=1
            while high<=r:
                lst.append(arr[high])
                high+=1
            for i in range(l,r+1):
                arr[i]=lst[i-l]
            return tot
        def mergesort(l,r,arr):
            if l>=r:
                return 0
            cnt=0
            mid=(l+r)//2
            cnt+=mergesort(l,mid,arr)
            cnt+=mergesort(mid+1,r,arr)
            cnt+=merge(l,mid,r,arr)
            return cnt
        return mergesort(0,len(arr)-1,arr)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a))
        print("~")

# } Driver Code Ends