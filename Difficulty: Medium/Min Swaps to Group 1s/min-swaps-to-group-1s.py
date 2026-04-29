class Solution:
    def minSwaps(self, arr):
        # code here
        n=len(arr)
        k=arr.count(1)
        if k==0:
            return -1
        cnt=0
        for i in range(k):
            if arr[i]==1:
                cnt+=1
        maxi=cnt
        for i in range(k,n):
            if arr[i]==1:
                cnt+=1
            if arr[i-k]==1:
                cnt-=1
            maxi=max(maxi,cnt)
        return k-maxi
        