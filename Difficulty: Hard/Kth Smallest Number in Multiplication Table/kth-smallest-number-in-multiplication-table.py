class Solution(object):
    def kthSmallest(self, m, n, k):
        #code here
        def func(ele):
            cnt=0
            for i in range(1,m+1):
                cnt+=min(ele//i,n)
            return cnt
        l,r=1,m*n
        while l<r:
            mid=(l+r)//2
            if func(mid)<k:
                l=mid+1
            else:
                r=mid
        return l