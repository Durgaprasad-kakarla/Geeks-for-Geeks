class Solution:
    def countXInRange(self, arr, queries):
        # code here\
        n=len(arr)
        def upper_bound(arr,l,r,ele):
            n=len(arr)
            while l<=r:
                mid=(l+r)//2
                if arr[mid]<=ele:
                    l=mid+1
                else:
                    r=mid-1
            return r
        def lower_bound(arr,l,r,ele):
            n=len(arr)
            while l<=r:
                mid=(l+r)//2
                if arr[mid]<ele:
                    l=mid+1
                else:
                    r=mid-1
            return r
        ans=[]
        for l,r,x in queries:
            lower=lower_bound(arr,l,r,x)
            upper=upper_bound(arr,l,r,x)
            ans.append(upper-lower)
        return ans
        