class Solution:
    def setMatrixZeroes(self, mat):
        # code here
        n,m=len(mat),len(mat[0])
        rows,columns=set(),set()
        for i in range(n):
            for j in range(m):
                if mat[i][j]==0:
                    rows.add(i)
                    columns.add(j)
        for i in range(n):
            for j in range(m):
                if i in rows or j in columns:
                    mat[i][j]=0
        return mat