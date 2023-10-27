#User function Template for python3

class Solution:
    def minimumNumberOfDeletions(self,s):
        # code here 
        n=len(s)
        s1=s
        s2=s[::-1]
        dp=[[0 for i in range(n+1)] for j in range(n+1)]
        for ind1 in range(1,n+1):
            for ind2 in range(1,n+1):
                if s1[ind1-1]==s2[ind2-1]:
                    dp[ind1][ind2]=1+dp[ind1-1][ind2-1]
                else:
                    dp[ind1][ind2]=max(dp[ind1-1][ind2],dp[ind1][ind2-1])
        return n-dp[n][n]
        '''def func(ind1,ind2,s1,s2,dp):
            if ind1==0 or ind2==0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if s1[ind1-1]==s2[ind2-1]:
                dp[ind1][ind2]= 1+func(ind1-1,ind2-1,s1,s2,dp)
                return dp[ind1][ind2]
            dp[ind1][ind2]=max(func(ind1-1,ind2,s1,s2,dp),func(ind1,ind2-1,s1,s2,dp))
            return dp[ind1][ind2]
        n=len(s)
        dp=[[-1 for i in range(n+1)]for j in range(n+1)]
        return n-func(n,n,s,s[::-1],dp)'''

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends