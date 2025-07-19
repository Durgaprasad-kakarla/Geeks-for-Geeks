class Solution:
    def vowelCount(self, s):
        #code here
        dic={}
        for i in s:
            if i in 'aeiou':
                if i in dic:
                    dic[i]+=1
                else:
                    dic[i]=1
        if len(dic)==0:
            return 0
        tot=1
        n=len(dic)
        for i in dic:
            tot*=(n*dic[i])
            n-=1
        return tot