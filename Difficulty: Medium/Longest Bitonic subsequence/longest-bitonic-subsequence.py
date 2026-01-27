class Solution:
    def longestBitonicSequence(self, n : int, nums : list[int]) -> int:
        # code here
        def lcs(nums):
            n=len(nums)
            dp=[1]*n
            for i in range(1,n):
                for j in range(i):
                    if nums[j]<nums[i]:
                        dp[i]=max(dp[i],dp[j]+1)
            return dp
        dp_left=lcs(nums)
        dp_right=lcs(nums[::-1])[::-1]
        # print(dp_left)
        # print(dp_right)
        maxi=0
        for i in range(n):
            if dp_left[i]>1 and dp_right[i]>1:
                maxi=max(maxi,dp_left[i]+dp_right[i]-1)
        return maxi
        ''' Time 
        
