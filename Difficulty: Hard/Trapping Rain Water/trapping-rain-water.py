class Solution:
    def maxWater(self, arr):
        # code here
        n=len(arr)
        pref=[0]*n
        maxi=0
        for i in range(n):
            pref[i]=max(maxi,arr[i])
            maxi=pref[i]
        tot=curr_max=0
        for i in range(n-1,-1,-1):
            curr_max=max(curr_max,arr[i])
            tot+=min(curr_max,pref[i])-arr[i]
        return tot