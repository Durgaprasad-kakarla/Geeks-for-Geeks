class Solution:
    def wildCard(self, txt, pat):
        # code here
        def check_all_stars(ind,s):
            n=len(s)
            for i in range(ind,-1,-1):
                if s[i]!='*':
                    return False
            return True
        def wildcard_matching(i,j,txt,pat):
            # print(i,j)
            if i<0 and j<0:
                return True
            if i<0 and j>=0:
                return check_all_stars(j,pat)
            if i>=0 and j<0:
                return False
            if dp[i][j]!=-1:
                return dp[i][j]
            if txt[i]==pat[j] or pat[j]=='?':
                dp[i][j]=wildcard_matching(i-1,j-1,txt,pat)
            elif pat[j]=='*':
                dp[i][j]= (wildcard_matching(i,j-1,txt,pat) or 
                        wildcard_matching(i-1,j,txt,pat) or 
                        wildcard_matching(i-1,j-1,txt,pat))
            else:
                dp[i][j]=False
            return dp[i][j]
        n,m=len(txt),len(pat)
        dp=[[-1 for _ in  range(m)] for _ in range(n)]
        return wildcard_matching(n-1,m-1,txt,pat)