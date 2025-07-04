from collections import defaultdict
class Solution:
    def countAtMostK(self, arr, k):
        # Code here
        n,start,dic,tot=len(arr),0,defaultdict(int),0
        for i in range(n):
            dic[arr[i]]+=1
            while start<n and len(dic)>k:
                dic[arr[start]]-=1
                if dic[arr[start]]==0:
                    del dic[arr[start]]
                start+=1
            tot+=(i-start+1)
        return tot