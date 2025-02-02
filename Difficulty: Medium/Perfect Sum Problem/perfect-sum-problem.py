#User function Template for python3
class Solution:
	def perfectSum(self, arr, target):
		# code here
		n=len(arr)
		def func(ind,target):
		    if ind<0:
		        if target==0:
		            return 1
		        return 0
		    if dp[ind][target]!=-1:
		        return dp[ind][target]
		    l=0
		    if target>=arr[ind]:
		        l=func(ind-1,target-arr[ind])
		    r=func(ind-1,target)
		    dp[ind][target]=l+r
		    return l+r
		dp=[[-1 for _ in range(target+1)] for _ in range(n)]
		cnt=func(n-1,target)
		return cnt


#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input().strip())  # Number of test cases
    while tc > 0:
        arr = list(map(int, input().strip().split()))  # Read array input
        target = int(input().strip())  # Read the target sum
        ob = Solution()  # Create the Solution object
        print(ob.perfectSum(arr, target))  # Call perfectSum with 2 arguments
        tc -= 1  # Decrease test case count
        print("~")
# } Driver Code Ends