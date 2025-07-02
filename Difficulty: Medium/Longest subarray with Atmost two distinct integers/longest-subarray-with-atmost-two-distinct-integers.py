from collections import defaultdict
class Solution:
    def totalElements(self, arr):
        # Code here
        dic={}
        n=len(arr)
        start,cnt,maxi=0,0,0
        for i in range(n):
            if arr[i] in dic:
                dic[arr[i]]+=1
            else:
                dic[arr[i]]=1
                cnt+=1
            while start<n and len(dic)>2:
                dic[arr[start]]-=1
                if dic[arr[start]]==0:
                    del dic[arr[start]]
                start+=1
            maxi=max(maxi,i-start+1)
        return maxi