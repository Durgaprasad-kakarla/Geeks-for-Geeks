#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def longestIncreasingSubsequence(self, n, arr):
        # Code here
        dp=[1]*n
        for i in range(1,n):
            for j in range(i):
                if arr[i]>arr[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        # print(dp)
        length,i=max(dp),n-1
        dic={}
        while i>=0:
            if dp[i]+1 in dic and dic[dp[i]+1]>arr[i]:
                dic[dp[i]]=arr[i]
            if dp[i]+1 not in dic:
                dic[dp[i]]=arr[i]
            i-=1
        return sorted(dic.values())

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.longestIncreasingSubsequence(N, arr)
        for val in res:
            print(val, end =' ')
        print()
# } Driver Code Ends