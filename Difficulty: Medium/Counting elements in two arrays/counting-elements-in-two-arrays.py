class Solution:
    def countLessEq(self, a, b):
        # code here
        def upperbound(arr,ele):
            n=len(arr)
            l,r=0,n-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]<=ele:
                    l=mid+1
                else:
                    r=mid-1
            return l
        b.sort()
        n=len(a)
        ans=[]
        for i in range(n):
            ans.append(upperbound(b,a[i]))
        return ans