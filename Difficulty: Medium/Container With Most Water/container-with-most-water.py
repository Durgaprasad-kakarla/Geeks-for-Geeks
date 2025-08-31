class Solution:
    def maxWater(self, arr):
        # code here
        n=len(arr)
        l,r=0,n-1
        maxi=0
        while l<r:
            maxi=max(maxi,min(arr[l],arr[r])*(r-l))
            if arr[l]<=arr[r]:
                l+=1
            else:
                r-=1
        return maxi