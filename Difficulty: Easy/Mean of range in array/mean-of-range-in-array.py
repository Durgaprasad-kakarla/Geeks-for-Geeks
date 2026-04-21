class Solution:
    def findMean(self, arr, queries):
        # code here
        n=len(arr)
        q=len(queries)
        pref=[0]*(n+1)
        for i in range(1,n+1):
            pref[i]=pref[i-1]+arr[i-1]
        ans=[]
        for l,r in queries:
            ans.append((pref[r+1]-pref[l])//(r-l+1))
        return ans