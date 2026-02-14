class Solution:
    def minTime (self, arr, k):
        # code here
        def minimum_time(arr,ele):
            sm,n,cnt=0,len(arr),0
            for i in range(n):
                sm+=arr[i]
                if sm>ele:
                    sm=arr[i]
                    cnt+=1
            return cnt+1 if sm>0 else cnt
        l,r=max(arr),sum(arr)
        while l<=r:
            mid=(l+r)//2
            if minimum_time(arr,mid)>k:
                l=mid+1
            else:
                r=mid-1
        return l
        