class Solution:
    def findMax(self, n, a, b, k):
        # code here
        pref=[0]*(n+1)
        for i in range(len(a)):
            # print(a[i],b[i])
            pref[a[i]]+=k[i]
            pref[b[i]+1]-=k[i]
        for i in range(1,n):
            pref[i]+=pref[i-1]
        return max(pref)