class Solution:    
    def ValidCorner(self,mat): 
        # Code here 
        n,m=len(mat),len(mat[0])
        def is_rectangle(row,col):
            for i in range(1,n+1):
                for j in range(1,m+1):
                    row1,col1=row+i,col
                    row2,col2=row,col+j
                    row3,col3=row+i,col+j
                    if row1<n and col1<m and mat[row1][col1]==1 and row2<n and col2<m and mat[row2][col2]==1 and row3<n and col3<m and mat[row3][col3]==1:
                        return True
            return False
        for i in range(n):
            for j in range(m):
                if mat[i][j]==1:
                    if is_rectangle(i,j):
                        return True
        return False