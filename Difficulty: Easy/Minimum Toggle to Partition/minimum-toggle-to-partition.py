class Solution:
    def minToggle(self, arr):
        # code here
        n=len(arr)
        cnt_1=arr.count(1)
        cnt_0=arr.count(0)
        mini=min(cnt_1,cnt_0)
        cnt=0
        for i in range(n):
            if arr[i]==1:
                cnt+=1
            curr=(n-i-1)
            mini=min(mini,cnt+curr-(cnt_1-cnt))
        if cnt==n:
            return 0
        return mini