class Solution:
    def combinations(self,ind,target,k,temp,ans):
        if len(temp)==k:
            if target==0:
                ans.append(temp.copy())
            return 
        if ind>9:
            return 
        if target>=ind:
            self.combinations(ind+1,target-ind,k,temp+[ind],ans)
        self.combinations(ind+1,target,k,temp,ans)
    def combinationSum(self, n, k):
        # code here
        ans=[]
        self.combinations(1,n,k,[],ans)
        return ans
        