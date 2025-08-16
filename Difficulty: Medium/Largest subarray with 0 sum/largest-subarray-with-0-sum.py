class Solution:
    def maxLength(self, arr):
        # code here
        sm,maxi,n=0,0,len(arr)
        dic={0:-1}
        for i in range(n):
            sm+=arr[i]
            if sm in dic:
                maxi=max(maxi,i-dic[sm])
            else:
                dic[sm]=i
        return maxi
        