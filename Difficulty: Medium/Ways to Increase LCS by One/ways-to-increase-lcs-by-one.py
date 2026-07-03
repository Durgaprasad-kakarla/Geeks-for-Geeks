class Solution:
    def waysToIncreaseLCSBy1(self, s1, s2):
        # code here
        n = len(s1)
        m = len(s2)


        pref = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if s1[i] == s2[j]:
                    pref[i + 1][j + 1] = pref[i][j] + 1
                else:
                    pref[i + 1][j + 1] = max(pref[i][j + 1], pref[i + 1][j])

       
        suf = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if s1[i] == s2[j]:
                    suf[i][j] = suf[i + 1][j + 1] + 1
                else:
                    suf[i][j] = max(suf[i + 1][j], suf[i][j + 1])

        lcs = pref[n][m]
        ans = 0

        
        for pos in range(n + 1):
            used = [False] * 26

            for j in range(m):
                c = ord(s2[j]) - ord('a')
                if used[c]:
                    continue

                if pref[pos][j] + 1 + suf[pos][j + 1] == lcs + 1:
                    used[c] = True
                    ans += 1

        return ans