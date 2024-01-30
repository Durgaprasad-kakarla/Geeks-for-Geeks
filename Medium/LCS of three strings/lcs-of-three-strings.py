#User function Template for python3

class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
        # code here
        def func(i,j,k,dp):
            if i<0 or j<0 or k<0:
                return 0
            if dp[i][j][k]!=-1:
                return dp[i][j][k]
            if A[i]==B[j] and B[j]==C[k]:
                dp[i][j][k]=1+func(i-1,j-1,k-1,dp)
                return dp[i][j][k]
            dp[i][j][k]=max(func(i-1,j,k,dp),func(i,j-1,k,dp),func(i,j,k-1,dp))
            return dp[i][j][k]
        dp=[[[-1 for i in range(n3)] for j in range(n2)] for k in range(n1)]
        return func(n1-1,n2-1,n3-1,dp)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n1,n2,n3 = map(int,input().split())
        A,B,C = input().split()

        solObj = Solution()

        ans = solObj.LCSof3(A,B,C,n1,n2,n3)

        print(ans)
# } Driver Code Ends