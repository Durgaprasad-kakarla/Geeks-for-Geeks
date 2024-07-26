#User function Template for python3

class Solution:
    def countMin(self, s):
        # code here
        def LCS(ind1,ind2,s1,s2,dp):
            if ind1<0 or ind2<0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if s1[ind1]==s2[ind2]:
                dp[ind1][ind2]=1+LCS(ind1-1,ind2-1,s1,s2,dp)
                return dp[ind1][ind2]
            dp[ind1][ind2]=max(LCS(ind1-1,ind2,s1,s2,dp),LCS(ind1,ind2-1,s1,s2,dp))
            return dp[ind1][ind2]
        n=len(s)
        dp=[[-1 for i in range(n)] for j in range(n)]
        max_sub=LCS(n-1,n-1,s,s[::-1],dp)
        return n-max_sub


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        Str = input()

        solObj = Solution()

        print(solObj.countMin(Str))

# } Driver Code Ends