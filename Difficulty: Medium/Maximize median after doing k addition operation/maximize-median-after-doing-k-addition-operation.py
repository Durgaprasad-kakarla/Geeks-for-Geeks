class Solution:
    def maximizeMedian(self, arr, k):
        # code here
        arr.sort()
        def increment_elements(arr,ele):
            n=len(arr)
            median_ind=(n//2) if n%2 else n//2-1
            tot=0
            for i in range(median_ind,n):
                if ele>arr[i]:
                    tot+=(ele-arr[i])
                    arr[i]=ele
            median=(arr[median_ind]+arr[median_ind+1])//2 if n%2==0 else arr[median_ind]
            return tot,median
        l,r=arr[0],arr[-1]+k
        ans=-1
        while l<=r:
            mid=(l+r)//2
            tot,median=increment_elements(arr.copy(),mid)
            if tot<=k:
                ans=median
                l=mid+1
            else:
                r=mid-1
        return ans
