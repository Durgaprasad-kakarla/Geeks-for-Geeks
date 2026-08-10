class Solution:
    def maxTask(self, high: list[int], low: list[int]) -> int:
        # code here
        def max_task(ind,prev):
            if ind==n:
                return 0
            if dp[ind][prev]!=-1:
                return dp[ind][prev]
            if prev:
                l=low[ind]+max_task(ind+1,1)
                r=max_task(ind+1,0)
                dp[ind][prev]=max(l,r)
                return max(l,r)
            else:
                l=low[ind]+max_task(ind+1,1)
                r=high[ind]+max_task(ind+1,1)
                k=max_task(ind+1,0)
                dp[ind][prev]=max(l,r,k)
                return max(l,r,k)
        n=len(high)
        dp=[[-1 for _ in range(2)] for _ in range(n)]
        return max(max_task(0,1),max_task(0,0))