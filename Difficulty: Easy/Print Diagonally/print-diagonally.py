class Solution:
    def diagView(self, mat): 
        # code here 
        n,m=len(mat),len(mat[0])
        def anti_diagonal(i,j):
            lst=[]
            while i<n and j>=0:
                lst.append(mat[i][j])
                i+=1
                j-=1
            return lst
        top_to_bottom=[]
        for i in range(m):
            top_to_bottom+=anti_diagonal(0,i)
        for i in range(1,n):
            top_to_bottom+=anti_diagonal(i,m-1)
        return top_to_bottom
        