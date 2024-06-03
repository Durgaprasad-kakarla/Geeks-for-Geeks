#User function Template for python3
class Solution:
    def numberOfConsecutiveOnes (ob,n):
        # code here 
        dp=[0]*(n+1)
        a,b=0,1
        dp[0],dp[1],dp[2]=0,0,1
        for i in range(3,n+1):
            c=(a+b)%(10**9+7)
            dp[i]=(dp[i-1]*2+c)%(10**9+7)
            a=b
            b=c
        return dp[n]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        N = int(input())

        ob = Solution()
        print(ob.numberOfConsecutiveOnes(N))

# } Driver Code Ends