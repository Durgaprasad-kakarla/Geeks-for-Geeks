class Solution:
    def maxSubarrayXOR(self, arr, k):
        # code here
        n=len(arr)
        xor=0
        for i in range(k):
            xor^=arr[i]
        maxi=xor
        for i in range(k,n):
            xor=xor^arr[i]^arr[i-k]
            maxi=max(maxi,xor)
        return maxi
        
       