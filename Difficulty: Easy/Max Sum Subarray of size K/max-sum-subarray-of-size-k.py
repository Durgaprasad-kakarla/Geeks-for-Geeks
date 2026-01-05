class Solution:
    def maxSubarraySum(self, arr, k):
        # code here 
        n=len(arr)
        window_sum=sum(arr[:k])
        max_sum=window_sum
        for i in range(k,n):
            window_sum=window_sum-arr[i-k]+arr[i]
            max_sum=max(max_sum,window_sum)
        return max_sum