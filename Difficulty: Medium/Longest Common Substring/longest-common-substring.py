#User function Template for python3

class Solution:
    def longestCommonSubstr(self, str1, str2):
        # code here
        n,m=len(str1),len(str2)
        dp=[[0 for i in range(m+1)] for j in range(n+1)]
        maxi=0
        for i in range(1,n+1):
            for j in range(1,m+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]+=dp[i-1][j-1]+1
                    maxi=max(maxi,dp[i][j])
        return maxi
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1 = input().strip()
        S2 = input().strip()
        ob = Solution()
        print(ob.longestCommonSubstr(S1, S2))

# } Driver Code Ends