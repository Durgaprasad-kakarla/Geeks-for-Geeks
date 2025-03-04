class Solution:
    def lis(self, arr):
        # code here
        n=len(arr)
        dp=[1]*n
        for i in range(n):
            for j in range(i):
                if arr[i]>arr[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)


#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    for _ in range(int(input())):
        a = [int(x) for x in input().split()]
        ob = Solution()
        print(ob.lis(a))
        print("~")
# } Driver Code Ends