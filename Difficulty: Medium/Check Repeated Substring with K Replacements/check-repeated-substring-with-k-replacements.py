class Solution:
    def kSubstr(self, s: str, k: int) -> bool:
        # code here
        n=len(s)
        dic={}
        for i in range(0,n,k):
            if s[i:i+k] in dic:
                dic[s[i:i+k]]+=1
            else:
                dic[s[i:i+k]]=1
        # print(dic)
        if len(dic)<=2:
            cnt=0
            for i in dic:
                if dic[i]>1:
                    cnt+=1
            if cnt>1:
                return False
            return True
        return False