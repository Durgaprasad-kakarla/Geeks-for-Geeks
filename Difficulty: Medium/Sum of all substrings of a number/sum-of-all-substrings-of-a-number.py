class Solution:
    def sumSubstrings(self,s):
        # code here
        n=len(s)
        tot=0
        for i in range(n):
            for j in range(i,n):
                tot+=int(s[i:j+1])
        return tot