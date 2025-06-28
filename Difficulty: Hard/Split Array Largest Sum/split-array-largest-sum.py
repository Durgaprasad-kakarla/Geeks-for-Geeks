class Solution:
    def splitArray(self, arr, k):
        # code here
        def func(arr,ele):
            cnt,n,sm=0,len(arr),0
            for i in range(n):
                sm+=arr[i]
                if sm>ele:
                    sm=arr[i]
                    cnt+=1
            return cnt+1 if sm>0 else cnt
        l,r=max(arr),sum(arr)
        while l<=r:
            mid=(l+r)//2
            if func(arr,mid)<=k:
                r=mid-1
            else:
                l=mid+1
        return l