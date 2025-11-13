class Solution:
    def isInterleave(self, s1, s2, s3):
        # code here
        n,m,k=len(s1),len(s2),len(s3)
        if n+m!=k:
            return False
        i,j=0,0
        while i<n and j<k:
            if s1[i]==s3[j]:
                i+=1
                j+=1
            else:
                j+=1
        if i<n:
            return False
        i,j=0,0
        while i<m and j<k:
            if s2[i]==s3[j]:
                i+=1
                j+=1
            else:
                j+=1
        if i<m:
            return False
        return True