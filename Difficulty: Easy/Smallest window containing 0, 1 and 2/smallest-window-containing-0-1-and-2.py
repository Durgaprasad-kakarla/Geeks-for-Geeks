class Solution:
    def smallestSubstring(self, s):
        # code here
        n=len(s)
        dic,start={},0
        mini=float('inf')
        for i in range(n):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
            while len(dic)==3 and start<n:
                # print(i,start)
                mini=min(mini,i-start+1)
                dic[s[start]]-=1
                if dic[s[start]]==0:
                    del dic[s[start]]
                start+=1
            
        return mini if mini!=float('inf') else -1