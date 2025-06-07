class Solution:
    def longestCommonSum(self, a1, a2):
        #Code here.
        n=len(a1)
        dic={0:-1}
        sm,maxi=0,0
        for i in range(n):
            sm+=a1[i]-a2[i]
            if sm in dic:
                maxi=max(maxi,i-dic[sm])
            else:
                dic[sm]=i
        return maxi