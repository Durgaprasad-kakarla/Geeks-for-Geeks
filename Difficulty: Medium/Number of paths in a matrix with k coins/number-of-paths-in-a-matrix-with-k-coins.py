class Solution:
    def numberOfPath(self, mat, k):
        # code here
        def path(row,col,target):
            # print(row,col,target)
            if row==0 and col==0:
                if target==mat[row][col]:
                    return 1
                return 0
            if target<0 or row<0 or col<0:
                return 0
            if dp[row][col][target]!=-1:
                return dp[row][col][target]
            l=path(row-1,col,target-mat[row][col])
            r=path(row,col-1,target-mat[row][col])
            dp[row][col][target]=l+r
            return l+r
        n,m=len(mat),len(mat[0])
        dp=[[[-1 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
        return path(n-1,m-1,k)
        

