#User function Template for python3
class Solution:
	
	def findMaxSum(self,arr, n):
		# code here
		dp=[0]*n
		dp[0]=arr[0]
		for i in range(1,n):
		    l=0
		    if i>1:
		        l=arr[i]+dp[i-2]
		    r=dp[i-1]
		    dp[i]=max(l,r,arr[i])
		return dp[n-1]
		
		
		
		
# 		def func(ind,arr,dp):
# 		    if ind==0:
# 		        return arr[0]
# 		    if ind<0:
# 		        return 0
# 		    if dp[ind]!=-1:
# 		        return dp[ind]
# 		    #not pick
# 		    l=arr[ind]+func(ind-2,arr,dp)
# 		    r=func(ind-1,arr,dp)
# 		    dp[ind]=max(l,r)
# 		    return max(l,r)
# 		dp=[-1 for i in range(n)]
# 		return func(n-1,arr,dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.findMaxSum(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends