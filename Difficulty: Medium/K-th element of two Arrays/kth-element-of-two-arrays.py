#User function Template for python3


class Solution:

    def kthElement(self, nums1,nums2, k):
        n,m=len(nums1),len(nums2)
        if n>m:
            return self.kthElement(nums2,nums1,k)
        l = max(0, k - m)
        r = min(k,n)
        while l<=r:
            mid1=(l+r)//2
            mid2=(k-mid1)
            l1,l2,r1,r2=-float('inf'),-float('inf'),float('inf'),float('inf')
            if mid1<n:
                r1=nums1[mid1]
            if mid2<m:
                r2=nums2[mid2]
            if mid1-1>=0:
                l1=nums1[mid1-1]
            if mid2-1>=0:
                l2=nums2[mid2-1]
            if l1>r2:
                r=mid1-1
            elif l2>r1:
                l=mid1+1
            else:
                return  max(l1,l2)
        return -1
