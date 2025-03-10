class Solution:
	def editDistance(self, s1, s2):
		# Code here
        def func(i,j,dp):
            if i<0:
                return j+1
            if j<0:
                return i+1
            if dp[i][j]!=-1:
                return dp[i][j]
            if s1[i]==s2[j]:
                dp[i][j]=func(i-1,j-1,dp)
                return dp[i][j]
            dp[i][j]=min(1+func(i,j-1,dp),1+func(i-1,j,dp),1+func(i-1,j-1,dp))
            return dp[i][j]
        dp=[[-1 for i in range(len(s2))] for j in range(len(s1))]
        return func(len(s1)-1,len(s2)-1,dp)

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s1 = input()
        s2 = input()
        ob = Solution()
        ans = ob.editDistance(s1, s2)
        print(ans)
        print("~")

# } Driver Code Ends