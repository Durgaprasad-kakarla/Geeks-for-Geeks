from itertools import accumulate
from bisect import bisect_left, bisect_right
class Solution:
    def minimumCoins(self, arr, k):
        # code here
        
        arr.sort()
        
        prefix_sum = list(accumulate(arr, initial=0))
        n = len(arr)
        ans = float('inf')
        for h in range(0, arr[-1]+1):
            i = bisect_left(arr, h) 
            cost1 = prefix_sum[i]
            j = bisect_right(arr, h+k)
            
            diff = prefix_sum[-1] - prefix_sum[j] 
            cost2 = diff - (n-j)*(h+k)
            ans = min(ans, cost1+cost2)
        
        return ans