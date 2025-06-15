class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        n=len(arr)
        if n<k:
            return -1
        def allocate_books(arr,ele):
            n=len(arr)
            sm=cnt=0
            for i in range(n):
                if sm+arr[i]>ele:
                    sm=arr[i]
                    cnt+=1
                else:
                    sm+=arr[i]
            if sm>0:
                cnt+=1
            return cnt
        l,r=max(arr),sum(arr)
        while l<=r:
            mid=(l+r)//2
            if allocate_books(arr,mid)>k:
                l=mid+1
            else:
                r=mid-1
        return l
