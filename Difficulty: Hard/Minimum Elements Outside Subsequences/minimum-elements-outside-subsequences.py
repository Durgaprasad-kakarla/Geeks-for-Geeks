from functools import cache
class Solution:
    def minCount(self, arr):
        """ code here """
        n = len(arr)

        @cache
        def dfs(i: int = 0, inc: int = -1, dec: int = -1) -> int:
            if i == n:
                return 0
            used = dfs(i + 1, inc, dec)
            a = arr[i]
            if inc == -1 or a > inc:
                used = max(used, 1 + dfs(i + 1, a, dec))
            if dec == -1 or a < dec:
                used = max(used, 1 + dfs(i + 1, inc, a))
            return used

        return n - dfs()
