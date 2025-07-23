class Solution:
    def subarraySum(self, arr):
        # code here 
        tot,n=0,len(arr)
        for i in range(n):
            tot+=(arr[i]*(i+1)*(n-i))
        return tot