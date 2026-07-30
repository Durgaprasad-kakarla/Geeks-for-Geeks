class Solution:
    def maxSubsetXOR(self, arr):
        # code here
        basis = [0] * 21
        for x in arr:
            for i in range(20, -1, -1):
                if (x >> i) & 1:
                    if basis[i]:
                        x ^= basis[i]
                    else:
                        basis[i] = x
                        break
        ans = 0
        for i in range(20, -1, -1):
            ans = max(ans, ans ^ basis[i])
        return ans

