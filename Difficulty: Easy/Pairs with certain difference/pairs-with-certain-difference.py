class Solution:
    def sumDiffPairs(self, arr, k):
        # code here
        n=len(arr)
        arr.sort(reverse=True)
        i=1
        total=0
        while i<n:
            if arr[i-1]-arr[i]<k:
                total+=arr[i]+arr[i-1]
                i+=2
            else:
                i+=1
        return total
        