class Solution:
    def getCount(self, n, d):
        # code here 
        if n <= d:
            return 0
        l,r = 1, n + 1
        while l < r:
            mid = l + (r - l) // 2
            if mid - sum(map(int, str(mid))) >= d:
                r = mid
            else:
                l = mid + 1
        return n - l + 1