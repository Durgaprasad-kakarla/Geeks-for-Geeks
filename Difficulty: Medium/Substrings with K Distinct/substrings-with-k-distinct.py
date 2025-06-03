class Solution:
    def countSubstr (self, s, k):
        # Code here
        def count_subarrays_atleastK(s,k):
            n=len(s)
            dic,start,tot={},0,0
            for i in range(n):
                if s[i] in dic:
                    dic[s[i]]+=1
                else:
                    dic[s[i]]=1
                while start<n and len(dic)>=k:
                    tot+=(n-i)
                    dic[s[start]]-=1
                    if dic[s[start]]==0:
                        del dic[s[start]]
                    start+=1
                # print(dic,tot)
            return tot
        return count_subarrays_atleastK(s,k)-count_subarrays_atleastK(s,k+1)