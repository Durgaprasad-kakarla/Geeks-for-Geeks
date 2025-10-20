from functools import lru_cache
from bisect import bisect_left
        
class Solution:
    def countBSTs(self, arr):
        # Code here
        @lru_cache(None)
        def count(n):
            """given a number of node, how many bst can be formed"""
            if n == 0 or n == 1:
                return 1
            return sum(count(i)*count(n-1-i) for i in range(n))
            
        sarr = list(sorted(arr))
        
        ans = []
        for e in arr:
            left = bisect_left(sarr, e)
            right = len(sarr) - 1 - left
            ans.append(count(left)*count(right))
        return ans