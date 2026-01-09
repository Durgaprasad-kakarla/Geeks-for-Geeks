class Solution:
    def countAtMostK(self, arr, k):
        # Code here
        n=len(arr)
        dic={}
        start,tot=0,0
        for i in range(n):
            while start<n and len(dic)<=k:
                if arr[start] in dic:
                    dic[arr[start]]+=1
                else:
                    if len(dic)<k:
                        dic[arr[start]]=1
                    else:
                        break
                start+=1
            # print(start,i,dic)
            tot+=(start-i)
            dic[arr[i]]-=1
            if dic[arr[i]]==0:
                del dic[arr[i]]
        return tot
        