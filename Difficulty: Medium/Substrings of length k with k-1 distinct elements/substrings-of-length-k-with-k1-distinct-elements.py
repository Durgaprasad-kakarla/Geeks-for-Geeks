class Solution:
    def substrCount(self, s, k):
        # code here
        n=len(s)
        dic={}
        for i in range(k):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
        tot=0
        if len(dic)==k-1:
            tot+=1
        for i in range(k,n):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
            dic[s[i-k]]-=1
            if dic[s[i-k]]==0:
                del dic[s[i-k]]
            if len(dic)==k-1:
                tot+=1
        return tot
        