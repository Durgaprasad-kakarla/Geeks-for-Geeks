class Solution:
    def getMinDiff(self, arr, k):
        # code here
        n=len(arr)
        arr.sort()
        maxi,mini=arr[-1]-k,arr[0]+k
        ans=arr[-1]-arr[0]
        for i in range(n-1):
            curr_maxi=max(maxi,arr[i]+k)
            curr_mini=min(mini,arr[i+1]-k)
            if curr_mini>=0:
                ans=min(ans,curr_maxi-curr_mini)
        return ans
        