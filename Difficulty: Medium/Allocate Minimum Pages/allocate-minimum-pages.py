class Solution:
    def findPages(self, arr, k):
        # code here
        n=len(arr)
        def cnt_pages(arr,atmost_pages):
            n=len(arr)
            sm,cnt=0,0
            for i in range(n):
                sm+=arr[i]
                if sm>atmost_pages:
                    cnt+=1
                    sm=arr[i]
            return cnt+1 if sm>0 else cnt
        l,r=max(arr),sum(arr)
        if n<k:
            return -1
        while l<=r:
            mid=(l+r)//2
            if cnt_pages(arr,mid)>k:
                l=mid+1
            else:
                r=mid-1
        return l
            