class Solution:
    def searchInsertK(self, arr, k):
        # code here
        n=len(arr)
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==k:
                return mid
            if arr[mid]<=k:
                l=mid+1
            else:
                r=mid-1
        return l
        