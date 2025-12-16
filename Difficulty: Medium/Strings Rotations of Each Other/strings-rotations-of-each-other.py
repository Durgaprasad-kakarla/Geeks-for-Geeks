class Solution:
    def areRotations(self, s1, s2):
        # code here
        n,m=len(s1),len(s2)
        s=s1+s1
        return s2 in s