#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def minimizeCost(self, k, arr):
        # code here
        def func(ind,k,dp):
            if ind==0:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            mini=float('inf')
            for i in range(1,k+1):
                if (ind-i)>=0:
                    mini=min(mini,abs(arr[ind]-arr[ind-i])+func(ind-i,k,dp))
            dp[ind]=mini
            return mini
        n=len(arr)
        dp=[-1]*n
        return func(n-1,k,dp)

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k= int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minimizeCost(k,arr)
        print(res)
        t -= 1


# } Driver Code Ends