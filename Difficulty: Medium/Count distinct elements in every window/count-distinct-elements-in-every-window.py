class Solution:
    def countDistinct(self, arr, k):
        # Code here
        n=len(arr)
        dic={}
        ans=[]
        cnt=0
        for i in range(k):
            if arr[i] in dic:
                dic[arr[i]]+=1
            else:
                cnt+=1
                dic[arr[i]]=1
        ans.append(cnt)
        for i in range(k,n):
            dic[arr[i-k]]-=1
            if dic[arr[i-k]]==0:
                cnt-=1
            if arr[i] in dic and dic[arr[i]]>0:
                dic[arr[i]]+=1
                ans.append(cnt)
            else:
                cnt+=1
                dic[arr[i]]=1
                ans.append(cnt)
        return ans
            

        