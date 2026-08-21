from collections import Counter
class Solution:
    def transform(self, s1, s2): 
        #code here
        if Counter(s1)!=Counter(s2):
            return -1
        n=len(s1)
        j=n-1
        for i in range(n-1,-1,-1):
            if s1[i]==s2[j]:
                j-=1
        return j+1