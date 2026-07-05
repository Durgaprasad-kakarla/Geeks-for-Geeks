class Solution:

    def maxCharGap(self, s: str) -> int:
        # code here
        n=len(s)
        chars=[-1]*26
        maxi=-1
        for i in range(n):
            if chars[ord(s[i])-97]==-1:
                chars[ord(s[i])-97]=i
            else:
                maxi=max(maxi,i-chars[ord(s[i])-97]-1)
        return maxi