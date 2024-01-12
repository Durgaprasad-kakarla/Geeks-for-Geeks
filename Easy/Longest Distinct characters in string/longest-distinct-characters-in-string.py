#User function Template for python3

class Solution:

    def longestSubstrDistinctChars(self, S):
        # code here
        dic={}
        n=len(S)
        j=0
        maxi=0
        for i in range(n):
            while j<n and S[j] not in dic:
                dic[S[j]]=1
                j+=1
            maxi=max(maxi,j-i)
            del dic[S[i]]
        return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()

        solObj = Solution()

        ans = solObj.longestSubstrDistinctChars(S)

        print(ans)

# } Driver Code Ends