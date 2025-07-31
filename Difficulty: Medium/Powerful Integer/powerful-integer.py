from heapq import heappush,heappop
class Solution:
    def powerfulInteger(self, intervals, k):
        # code here
        intervals.sort()
        q, ans = [], -1
        for start, end in intervals:
            while q and q[0] < start:
                heappop(q)
            heappush(q, end)
            while len(q) >= k:
                ans = max(ans, heappop(q))
    
        while len(q) >= k:
            ans = max(ans, q[0])
            heappop(q)
        
        return ans
