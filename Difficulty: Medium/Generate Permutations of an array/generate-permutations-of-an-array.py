class Solution:
    def permuteDist(self, arr):
        # code here
        n=len(arr)
        def permutations(ind,temp):
            if ind==len(temp)-1:
                ans.append(temp.copy())
                return 
            permutations(ind+1,temp)
            for i in range(ind+1,n):
                temp[i],temp[ind]=temp[ind],temp[i]
                permutations(ind+1,temp)
                temp[i],temp[ind]=temp[ind],temp[i]
        ans=[]
        permutations(0,arr)
        return ans
        
        
        