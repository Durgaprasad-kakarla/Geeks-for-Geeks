import heapq
class Solution:
    def overlapInt(self, arr):
        # code here
        n,maxi=len(arr),max([i[1] for i in arr])
        pref=[0]*(maxi+2)
        for l,r in arr:
            pref[l-1]+=1
            pref[r]-=1
        for i in range(1,maxi+1):
            pref[i]+=pref[i-1]
        ans=-1
        for i in range(maxi+1):
            ans=max(ans, pref[i])
        return ans