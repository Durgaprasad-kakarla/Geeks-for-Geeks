class Solution:
    def replaceElements(self, nums):
        # code here
        n=len(nums)
        arr=nums.copy()
        ans=[]
        nums[0]=arr[0]^arr[1]
        for i in range(1,n-1):
            nums[i]=arr[i-1]^arr[i+1]
        nums[n-1]=(arr[n-1]^arr[n-2])
        return ans