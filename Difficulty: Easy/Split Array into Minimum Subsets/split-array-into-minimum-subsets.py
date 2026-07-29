class Solution:
    def minSubsets(self, arr):
        #code here
        n=len(arr)
        arr.sort()
        cnt=1
        for i in range(1,n):
            if arr[i]!=arr[i-1]+1:
                cnt+=1
        return cnt