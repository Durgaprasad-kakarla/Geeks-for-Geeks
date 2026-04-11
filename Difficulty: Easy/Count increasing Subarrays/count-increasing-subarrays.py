class Solution:
    def countIncreasing(self, arr):
        # code here.
        n=len(arr)
        cnt=1
        tot=0
        for i in range(1,n):
            if arr[i-1]<arr[i]:
                cnt+=1
                tot+=cnt-1
            else:
                cnt=1
            # print(cnt,tot)
        return tot
            