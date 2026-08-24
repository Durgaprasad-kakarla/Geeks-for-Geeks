class Solution:
    def prefixStrings(self, n: int) -> int:
        # code here
        mod=10**9+7
        ans=1
        for i in range(1,n+1):
            ans=(ans*(n+i))//i
        return (ans//(n+1))%mod