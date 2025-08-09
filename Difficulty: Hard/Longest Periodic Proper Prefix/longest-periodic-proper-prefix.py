class Solution:
    def getLongestPrefix(self, s):
        # code here
        n = len(s)
        lsp = [0]*n
        for i in range(1, n):
            j = lsp[i-1]
            while j > 0 and s[i] != s[j]:
                j = lsp[j-1]
            if s[i] == s[j]:
                j += 1
            lsp[i] = j
        j = lsp[-1]
        r = float('inf')
        while j > 0:
            r = min(r, j)
            j = lsp[j-1]
        if r == float('inf'):
            return -1
        return n-r
        
