class Solution:
    def findIndex(self, s):
        # code here 
        n=len(s)
        suff=[0]*n
        if s[-1]==')':
            suff[n-1]=1
        for i in range(n-2,-1,-1):
            suff[i]+=suff[i+1]+(1 if s[i]==')' else 0)
        pref=0
        for i in range(n):
            if pref==suff[i]:
                return i
            pref+=(1 if s[i]=='(' else 0)
        return n