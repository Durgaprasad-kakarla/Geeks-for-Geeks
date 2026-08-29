class Solution:
    def countSubsequences(self, s, n):
        # code here
        mod = 10**9 + 7
        rems = [0] * n
        rems[0] = 1
        for c in s:
            d = ord(c) - ord("0")
            new_rems = rems.copy()
            for r in range(n):
                if rems[r] == 0: continue
                r1 = (r * 10 + d) % n
                new_rems[r1] = (new_rems[r1] + rems[r]) % mod
            rems = new_rems
        return rems[0] - 1