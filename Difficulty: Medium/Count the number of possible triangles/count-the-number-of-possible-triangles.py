class Solution:
    def countTriangles(self, arr):
        # code here
        arr.sort()
        n=len(arr)
        res=0
        for i in range(n-1,-1,-1):
            l,r=0,i-1
            while l<r:
                if arr[l]+arr[r]>arr[i]:
                    res+=(r-l)
                    r-=1
                else:
                    l+=1
        return res
