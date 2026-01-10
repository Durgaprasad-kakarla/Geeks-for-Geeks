class Solution:
    def countSubstr (self, s, k):
        # Code here
        def count_substr_atleast_k(s,k):
            n=len(s)
            dic={}
            start=tot=0
            for i in range(n):
                while start<n and len(dic)<k:
                    if s[start] in dic:
                        dic[s[start]]+=1
                    else:
                        dic[s[start]]=1
                    start+=1
                if len(dic)==k:
                    tot+=(n-start+1)
                dic[s[i]]-=1
                if dic[s[i]]==0:
                    del dic[s[i]]
            return tot
        return count_substr_atleast_k(s,k)-count_substr_atleast_k(s,k+1)
                