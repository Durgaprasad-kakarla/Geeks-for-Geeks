from bisect import bisect_left
class Solution:
    def binarySearchable(self, arr):
        # code here 
        n=len(arr)
        def binary_search(arr,ele):
            n=len(arr)
            l,r=0,n-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]==ele:
                    return True
                elif arr[mid]>ele:
                    r=mid-1
                else:
                    l=mid+1
            return False
        cnt=0
        for i in range(n):
            cnt+=(1 if binary_search(arr,arr[i]) else 0)
        return cnt