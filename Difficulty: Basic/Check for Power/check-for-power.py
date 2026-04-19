class Solution:
    def isPower(self, x, y):
        # code here
        if x==1:
            return y==1
        l,r=0,1000
        while l<=r:
            mid=(l+r)//2
            power=x**mid
            if power==y:
                return True
            elif power>y:
                r=mid-1
            else:
                l=mid+1
        return False
