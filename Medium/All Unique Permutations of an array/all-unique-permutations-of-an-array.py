#User function Template for python3

class Solution:
    def uniquePerms(self, nums, n):
        # code here 
        def recurpermute(ind,nums,ans):
            if ind==len(nums):
                ans.append(tuple(nums.copy()))
                return 
            for i in range(ind,len(nums)):
                nums[ind],nums[i]=nums[i],nums[ind]
                recurpermute(ind+1,nums,ans)
                nums[ind],nums[i]=nums[i],nums[ind]
        ans=[]
        recurpermute(0,nums,ans)
        return sorted(list(set(ans)))
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        res = ob.uniquePerms(arr,n)
        for i in range(len(res)):
            for j in range(n):
                print(res[i][j],end=" ")
            print()
# } Driver Code Ends