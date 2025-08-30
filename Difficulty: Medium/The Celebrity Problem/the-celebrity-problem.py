class Solution:
    def celebrity(self, mat):
        # code here
        n = len(mat)
        a, b = 0, n - 1
        
        while a < b:
            if mat[a][b] == 1:  
                a += 1
            else:
                b -= 1
        
        candidate = a
        
        for i in range(n):
            if i != candidate:
                if mat[candidate][i] or not mat[i][candidate]:
                    return -1
        return candidate