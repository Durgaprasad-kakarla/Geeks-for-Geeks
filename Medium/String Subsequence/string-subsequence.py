
class Solution:
    def countWays(self, s1 : str, s2 : str) -> int:
        # code here
        n,m=len(s1),len(s2)
        def count_subsequences(ind1,ind2,dp):
            if ind2<0:
                return 1
            if ind1<0:
                return 0
            if dp[ind1][ind2]!=-1:
                return dp[ind1][ind2]
            if s1[ind1]==s2[ind2]:
                dp[ind1][ind2]=count_subsequences(ind1-1,ind2-1,dp)+count_subsequences(ind1-1,ind2,dp)
                return dp[ind1][ind2]
            else:
                dp[ind1][ind2]=count_subsequences(ind1-1,ind2,dp)
                return dp[ind1][ind2]
        dp=[[-1 for i in range(m)] for j in range(n)]
        return count_subsequences(n-1,m-1,dp)%(10**9+7)



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        s1 = (input())

        s2 = (input())

        obj = Solution()
        res = obj.countWays(s1, s2)

        print(res)

# } Driver Code Ends