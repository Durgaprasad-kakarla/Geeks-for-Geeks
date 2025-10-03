class Solution:
    def possible(self,ind,s,ans,dic,arr):
        if ind==len(arr):
            ans.append(s)
            return 
        if arr[ind] in dic:
            for i in dic[arr[ind]]:
                self.possible(ind+1,s+i,ans,dic,arr)
        else:
            self.possible(ind+1,s,ans,dic,arr)
    def possibleWords(self, arr):
        # code here
        ans=[]
        dic={2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        self.possible(0,'',ans,dic,arr)
        return ans
