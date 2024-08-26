# your task is to complete this function
# function should return True/False or 1/0
# str1: pattern
# str2: text
class Solution:
    def wildCard(self,pattern, string):
        # Code here
        def isAllStars(s1,x):
            for i in range(x+1):
                if s1[i]!='*':
                    return False 
            return True
        def func(i,j,s1,s2,dp):
            if i<0 and j<0:
                return True
            if j>=0 and i<0:
                return False
            if i>=0 and j<0:
                return isAllStars(s1,i)
            if dp[i][j]!=-1:
                return dp[i][j]
            if s1[i]==s2[j] or s1[i]=='?':
                dp[i][j]=func(i-1,j-1,s1,s2,dp)
                return dp[i][j]
            elif s1[i]=='*':
                dp[i][j]=func(i-1,j,s1,s2,dp) or func(i,j-1,s1,s2,dp)
                return dp[i][j]
            dp[i][j]=False
            return False 
        n,m=len(pattern),len(string)
        dp=[[-1 for _ in range(m)] for _ in range(n)]
        return func(n-1,m-1,pattern,string,dp)



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        pattern = input().strip()
        string = input().strip()
        if Solution().wildCard(pattern, string):
            print(1)
        else:
            print(0)

# } Driver Code Ends