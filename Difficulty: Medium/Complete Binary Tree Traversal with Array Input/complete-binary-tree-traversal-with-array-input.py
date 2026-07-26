class Solution:
    def levelSort(self, arr):
        # code here
        n=len(arr)
        cnt=1
        ans=[]
        i=0
        while cnt<=n:
            ans.append(sorted(arr[i:i+cnt]))
            i=i+cnt
            cnt+=cnt
        return ans