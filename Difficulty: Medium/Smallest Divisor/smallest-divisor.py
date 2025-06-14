import math
class Solution:
    def smallestDivisor(self, arr, k):
        # Code here
        def ceil_total(n,arr,ele):
            cnt=0
            for i in range(n):
                cnt+=math.ceil(arr[i]/ele)
            return cnt
        n=len(arr)
        l,r=1,max(arr)
        while l<=r:
            mid=(l+r)//2
            if ceil_total(n,arr,mid)<=k:
                r=mid-1
            else:
                l=mid+1
        return l