#User function Template for python3

class Solution:
    def numberOfPaths (self, m, n):
        path = 1
        mod=10**9+7
        N=m+n-2
        r=m-1
        ans=1
        for i in range(1,r+1):
            ans=(ans*(N-i+1))%mod
            ans=(ans*pow(i,mod-2,mod))%mod
        return int(ans)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

        

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        M, N = map(int, input().split())
        ans = ob.numberOfPaths(M, N)
        print(ans)




# } Driver Code Ends