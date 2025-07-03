class Solution:
    def longestKSubstr(self, s, k):
        # code here
        n=len(s)
        dic,start,cnt,maxi={},0,0,-float('inf')
        for i in range(n):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
                cnt+=1
            while start<n and len(dic)>k:
                dic[s[start]]-=1
                if dic[s[start]]==0:
                    del dic[s[start]]
                start+=1
            if len(dic)==k:
                maxi=max(maxi,i-start+1)
        return maxi if maxi!=-float('inf') else -1
        
        