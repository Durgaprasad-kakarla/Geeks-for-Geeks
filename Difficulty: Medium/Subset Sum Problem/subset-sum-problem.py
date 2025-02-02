#User function Template for python3

class Solution:
    def isSubsetSum (self, arr, target):
        # code here 
        n=len(arr)
        dp=[[False for i in range(target+1)] for j in range(n+1)]
        for i in range(n):
            dp[i][0]=True
        for i in range(1,n+1):
            for j in range(1,target+1):
                l=False
                if j>=arr[i-1]:
                    l=dp[i-1][j-arr[i-1]]
                r=dp[i-1][j]
                dp[i][j]=l or r
        return dp[n][target]
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for itr in range(N):
            arr[itr] = int(arr[itr])
        sum = int(input())

        ob = Solution()
        if ob.isSubsetSum(arr, sum) == True:
            print("true")
        else:
            print("false")

        print("~")

# } Driver Code Ends