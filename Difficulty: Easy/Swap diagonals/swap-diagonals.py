class Solution:
    def swapDiagonal(self, mat):
        # code here
        n=len(mat)
        for i in range(n):
            mat[i][i],mat[i][n-i-1]=mat[i][n-i-1],mat[i][i]
        return mat
        '''
        0 1 2 3 
        4 5 6 7 
        8 9 3 5
        5 7 8 9'''
