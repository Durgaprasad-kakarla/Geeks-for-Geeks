class Solution:
    def matrixMultiplication(self, arr):
        # code here
        def multi(i,j):
            if i==j:
                return 0
            mini=float("inf")
            if dp[i][j]!=-1:
                return dp[i][j]
            for k in range(i,j):
                ans=multi(i,k)+multi(k+1,j)+arr[i-1]*arr[k]*arr[j]
                mini=min(mini,ans)
            dp[i][j]=mini
            return mini
        n=len(arr)
        dp=[[-1 for _ in range(n)] for _ in range(n)]
        return multi(1,n-1)
        


#{ 
 # Driver Code Starts
# Initial Template for Python 3

t = int(input())  # number of test cases
for _ in range(t):
    arr = list(map(int, input().split()))  # input array
    s = Solution().matrixMultiplication(arr)  # find the missing number
    print(s)  # print the result
    print("~")

# } Driver Code Ends