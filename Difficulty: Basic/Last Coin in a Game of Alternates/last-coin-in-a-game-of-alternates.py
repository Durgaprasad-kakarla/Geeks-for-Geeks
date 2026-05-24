class Solution:
    def coin(self, arr):
        # code here
        n=len(arr)
        l,r=0,n-1
        while l<r:
            if arr[l]>arr[r]:
                l+=1
            else:
                r-=1
        return arr[l]