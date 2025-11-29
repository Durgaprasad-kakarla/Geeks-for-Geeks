class Solution:
    def countSetBits(self,n):
        # code here
        cnt=0
        while n>1:
            x=int(math.log2(n))
            cnt+=(n-(1<<x))+(1<<(x-1))*x+1
            n-=(1<<x)
            if n==0:
                return cnt
        return cnt+1