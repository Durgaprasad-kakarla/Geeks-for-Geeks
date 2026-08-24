class Solution:
    def findPages(self, arr, k):
        # code here
        n=len(arr)
        if n<k:
            return -1
        def allocate_pages(pages):
            sm,books_cnt=0,0
            for i in range(n):
                sm+=arr[i]
                if sm>pages:
                    books_cnt+=1
                    sm=arr[i]
            return books_cnt+1
        l,r=max(arr),sum(arr)
        while l<=r:
            mid=(l+r)//2
            if allocate_pages(mid)>k:
                l=mid+1
            else:
                r=mid-1
        return l