class Solution:
    def nthRoot(self, n, m):
       # code here
        l,r=0,m
        while l<=r:
            mid=(l+r)//2
            curr=mid**n
            if curr==m:
                return mid
            elif curr<m:
                l=mid+1
            else:
                r=mid-1
        return -1