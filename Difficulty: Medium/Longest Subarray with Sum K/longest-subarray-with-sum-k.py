class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        n=len(arr)
        dic={0:-1}
        sm,maxi=0,0
        for i in range(n):
            sm+=arr[i]
            if sm-k in dic:
                maxi=max(maxi,i-dic[sm-k])
            if sm not in dic:
                dic[sm]=i
        return maxi
