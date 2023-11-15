#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def betterString(self, str1, str2):
        # Code here
        def distinctsubsequences(str1):
            n=len(str1)
            dp=[0]*(n+1)
            dic={}
            dp[0]=1
            i=1
            while i<(n+1):
                dp[i]=(dp[i-1]*2)
                c=str1[i-1]
                if c in dic:
                    dp[i]-=dp[dic[c]-1]
                dic[c]=i
                i+=1
            return dp[i-1]
        if distinctsubsequences(str1)>=distinctsubsequences(str2):
            return str1
        return str2

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str1 = input()
        str2 = input()
        ob = Solution()
        res = ob.betterString(str1, str2)
        print(res)
# } Driver Code Ends