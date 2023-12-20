#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minCandy(self, N, nums):
        # Code here
        n=len(nums)
        relate_to_left=[1]*n
        relate_to_right=[1]*n
        for i in range(1,n):
            if nums[i-1]<nums[i]:
                relate_to_left[i]=relate_to_left[i-1]+1
        for i in range(n-2,-1,-1):
            if nums[i]>nums[i+1]:
                relate_to_right[i]=relate_to_right[i+1]+1
        cnt=0
        for i in range(n):
            cnt+=max(relate_to_left[i],relate_to_right[i])
        return cnt

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        ratings = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCandy(N, ratings)
        print(res)
# } Driver Code Ends