class Solution:
    def applyDiff2D(self, mat, opr):
        # code here 
        n,m=len(mat),len(mat[0])
        new_mat=[[0 for _ in range(m+1)] for _ in range(n+1)]
        for ele,r1,c1,r2,c2 in opr:
            new_mat[r1][c1]+=ele
            new_mat[r1][c2+1]-=ele
            new_mat[r2+1][c1]-=ele
            new_mat[r2+1][c2+1]+=ele
        for i in range(1,m):
            new_mat[0][i]+=new_mat[0][i-1]
        for i in range(1,n):
            for j in range(1,m):
                new_mat[i][j]+=new_mat[i][j-1]
            for j in range(m):
                new_mat[i][j]+=new_mat[i-1][j]
        # print(new_mat)
        for i in range(n):
            for j in range(m):
                mat[i][j]+=new_mat[i][j]
        return mat