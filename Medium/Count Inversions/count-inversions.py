class Solution:
    #User function Template for python3
    
    # arr[]: Input Array
    # N : Size of the Array arr[]
    #Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        def merge(l,mid,r,arr):
            left,right=l,mid+1
            cnt=0
            lst=[]
            while left<=mid:
                while right<=r and arr[left]>arr[right]:
                    cnt+=(mid-left+1)
                    right+=1
                left+=1
            left,right=l,mid+1
            while left<=mid and right<=r:
                if arr[left]<=arr[right]:
                    lst.append(arr[left])
                    left+=1
                else:
                    lst.append(arr[right])
                    right+=1
            while left<=mid:
                lst.append(arr[left])
                left+=1
            while right<=r:
                lst.append(arr[right])
                right+=1
            for i in range(l,r+1):
                arr[i]=lst[i-l]
            return cnt
        def mergesort(l,r,arr):
            cnt=0
            if l>=r:
                return cnt
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

if __name__=='__main__':
    t = int(input())
    for tt in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        obj = Solution()
        print(obj.inversionCount(a,n))
# } Driver Code Ends