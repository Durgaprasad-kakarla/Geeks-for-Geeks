class Solution:
    def wifiRange(self, s, x):
        # code here
        n=len(s)
        suff=[-1]*n
        curr=-1
        for i in range(n-1,-1,-1):
            if s[i]=='1':
                curr=i
            suff[i]=curr
        # print(suff)
        pref=-1
        for i in range(n):
            if s[i]=='1':
                pref=i
            else:
                # print(suff,pref)
                if (suff[i]==-1 or i+x<suff[i]) and (pref==-1 or i-pref>x):
                    return False
        return True