class Solution:
    def maxMinDiff(self, arr, k):
        # code here
        arr.sort()
        def count_elements(diff,arr):
            cnt,ele=1,arr[0]
            n=len(arr)
            for i in range(1,n):
                if arr[i]-ele>=diff:
                    ele=arr[i]
                    cnt+=1
            return cnt
        l,r=0,arr[-1]-arr[0]
        while l<=r:
            mid=(l+r)>>1
            if count_elements(mid,arr)>=k:
                l=mid+1
            else:
                r=mid-1
        return r
