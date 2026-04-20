class Solution:
    def derangeCount(self, n: int) -> int:
        # code here
        if n==0:
            return 1
        if n==1:
            return 0
        prev1,prev2=0,1
        for i in range(2,n+1):
            curr=(i-1)*(prev1+prev2)
            prev2=prev1
            prev1=curr
        return curr