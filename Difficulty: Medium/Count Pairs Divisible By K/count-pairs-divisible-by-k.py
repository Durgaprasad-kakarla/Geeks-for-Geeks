class Solution:
    def countKdivPairs(self, arr, k):
        # code here
        n=len(arr)
        dic={}
        for i in range(n):
            arr[i]=arr[i]%k
            if arr[i] in dic:
                dic[arr[i]]+=1
            else:
                dic[arr[i]]=1
        # print(dic)
        tot=0
        if 0 in dic:
            tot+=(dic[0]*(dic[0]-1))//2
        for i in dic:
            if i<=k//2 and k-i in dic:
                if i!=k-i:
                    tot+=(dic[i]*dic[k-i])
                else:
                    tot+=(dic[i]*(dic[i]-1))//2
        return tot
        