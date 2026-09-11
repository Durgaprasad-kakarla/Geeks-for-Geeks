from math import gcd
class Solution:
    def sameMod(self, arr):
        # code here
        n = len(arr)
        g = 0
        for a in arr:
            g = gcd(g, abs(a - arr[0]))
        if g == 0:
            return -1
        div_count = 0
        i = 1
        while i * i < g:
            if g % i == 0:
                div_count += 2
            i += 1
        if i * i == g:
            div_count += 1
        return div_count