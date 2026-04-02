class Solution:
    def countWays(self,n,k):
        #code here.
        if k==1:
            if n<=2:
                return 1
            return 0
        if n==1:
            return k
        a=k
        b=k*k
        for i in range(n-2):
            c=((a+b)*(k-1))%(10**9+7)
            a=b
            b=c
        return b%(10**9+7)