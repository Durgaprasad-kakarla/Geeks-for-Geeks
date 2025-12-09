class Solution:
    def findDuplicates(self, arr):
        # code her
        n=len(arr)
        dic={}
        for i in arr:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        ans=[]
        for i in dic:
            if dic[i]>1:
                ans.append(i)
        return ans
        