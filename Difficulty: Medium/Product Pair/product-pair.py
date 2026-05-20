class Solution:
    def isProduct(self, arr, target):
        # code here
        dic={}
        n=len(arr)
        if target==0:
            if 0 in arr:
                return True
            return False
        for i in range(n):
            dic[arr[i]]=i
        for i in range(n):
            if arr[i]!=0 and (target%arr[i]==0 and target//arr[i] in dic):
                if dic[target//arr[i]]!=i:
                    return True
        return False
                