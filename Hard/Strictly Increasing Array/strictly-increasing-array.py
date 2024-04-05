#User function Template for python3

class Solution:
	def min_operations(self,nums):
		# Code here
		n=len(nums)
		dp=[1 for i in range(n)]
        maxi=1
        for i in range(n):
            for prev in range(i):
                if nums[prev]<nums[i] and i-prev<=nums[i]-nums[prev]:
                    dp[i]=max(dp[i],1+dp[prev])
            maxi=max(maxi,dp[i])
        return n-maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n = int(input())
		nums = list(map(int, input().split()))
		ob = Solution();
		ans = ob.min_operations(nums)
		print(ans)
# } Driver Code Ends