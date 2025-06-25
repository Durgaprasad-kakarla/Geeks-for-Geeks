class Solution:
    def sameFreq(self, s: str) -> bool:
        #code here
        n=len(s)
        dic={}
        for i in range(n):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
        if len(set((dic.values())))==1:
            return True
        for i in dic:
            dic[i]-=1
            prev,flag=-1,0
            for j in dic:
                if dic[j]!=0:
                    if prev==-1:
                        prev=dic[j]
                    elif prev!=dic[j]:
                        flag=1
                        break
            dic[i]+=1
            if flag==0:
                return True
        return False
        