class Solution:
    def maxSumWithK(self, arr: list[int], k: int) -> int:
        # code here
        n=len(arr)
        sm=0
        for i in range(k):
            sm+=arr[i]
        maxi=sm
        pref=0
        mini=float("inf")
        for i in range(k,n):
            pref+=arr[i-k]
            mini=min(mini,pref)
            sm+=arr[i]
            maxi=max(maxi,sm,sm-mini)
        return maxi