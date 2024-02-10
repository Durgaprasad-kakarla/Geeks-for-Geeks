#User function Template for python3

class Solution:
    def numberOfPath (self, n, k, arr):
        # code here
        def func(i,j,k,dp):
            if k<0:
                return 0
            if i==0 and j==0:
                if k==arr[0][0]:
                    return 1
                return 0
            if i<0 or j<0:
                return 0
            if dp[i][j][k]!=-1:
                return dp[i][j][k]
            l=func(i-1,j,k-arr[i][j],dp)
            r=func(i,j-1,k-arr[i][j],dp)
            dp[i][j][k]=l+r
            return l+r
        dp=[[[-1 for i in range(k+1)]for j in range(n)] for f in range(n)]
        return func(n-1,n-1,k,dp)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        k= int(input())
        n=int(input())
        l = list(map(int, input().split()))
        arr = list()
        c=0
        for i in range(0, n):
            temp = list()
            for j in range(0, n):
                temp.append(l[c])
                c += 1
            arr.append(temp)
        ans = ob.numberOfPath(n, k, arr);
        print(ans)


# } Driver Code Ends