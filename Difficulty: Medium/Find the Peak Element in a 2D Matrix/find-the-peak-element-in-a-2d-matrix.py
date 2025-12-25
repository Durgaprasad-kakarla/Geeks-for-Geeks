class Solution:
    def findPeakGrid(self, mat):
        # code here
        n,m=len(mat),len(mat[0])
        def check_peak(row,col):
            dr=[0,-1,0,1]
            dc=[1,0,-1,0]
            for i in range(4):
                nrow=row+dr[i]
                ncol=col+dc[i]
                if nrow>=0 and ncol>=0 and nrow<n and ncol<m:
                    if mat[nrow][ncol]>mat[row][col]:
                        return False
            return True
        for i in range(n):
            for j in range(m):
                if check_peak(i,j):
                    # print(mat[i][j])
                    return [i,j]
        return [-1,-1]