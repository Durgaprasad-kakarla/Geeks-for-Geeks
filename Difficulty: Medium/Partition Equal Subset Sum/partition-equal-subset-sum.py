class Solution:
    def equalPartition(self, arr):
        # code here
        n=len(arr)
        sm=sum(arr)
        if sm%2!=0:
            return False
        target=sm//2
        def equal_partition(ind,target):
            if ind==0:
                if target==arr[ind]:
                    return True
                return False
            if dp[ind][target]!=-1:
                return dp[ind][target]
            l=False
            if target>=arr[ind]:
                l=equal_partition(ind-1,target-arr[ind])
            r=equal_partition(ind-1,target)
            dp[ind][target]=l or r
            return l or r
        dp=[[-1 for _ in range(target+1)] for i in range(n)]
        return equal_partition(n-1,target)