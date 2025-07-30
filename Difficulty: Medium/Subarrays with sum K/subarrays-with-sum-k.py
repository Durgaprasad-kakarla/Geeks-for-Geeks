class Solution:
    def cntSubarrays(self, arr, k):
        # code here
        dic={0:1}
        sm,cnt,n=0,0,len(arr)
        for i in range(n):
            sm+=arr[i]
            if sm-k in dic:
                cnt+=(dic[sm-k])
            if sm in dic:
                dic[sm]+=1
            else:
                dic[sm]=1
        return cnt
        