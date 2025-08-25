class Solution:
    def isSubSeq(self, s1, s2):
        # code here
        n,m=len(s1),len(s2)
        i,j=0,0
        while i<n and j<m:
            if s1[i]==s2[j]:
                i+=1
                j+=1
            else:
                j+=1
        if i==n:
            return True
        return False
        