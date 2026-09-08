class Solution:
    def searchWord(self, mat, word):
        # code here
        def check_all_directions(row,col):
            i,j=row,col
            ind=0
            while (j<m and ind<len(word)) and mat[i][j]==word[ind]:
                j+=1
                ind+=1
            if ind==len(word):
                return True
            i,j=row,col
            ind=0
            while j>=0 and ind<len(word) and mat[i][j]==word[ind]:
                j-=1
                ind+=1
            if ind==len(word):
                return True
            i,j=row,col
            ind=0
            while i>=0 and ind<len(word) and mat[i][j]==word[ind]:
                i-=1
                ind+=1
            if ind==len(word):
                return True
            i,j=row,col
            ind=0
            while i<n and ind<len(word) and mat[i][j]==word[ind]:
                i+=1
                ind+=1
            if ind==len(word):
                return True
            i,j=row,col
            ind=0
            while (j<m and i<n) and ind<len(word) and mat[i][j]==word[ind]:
                i+=1
                j+=1
                ind+=1
            if ind==len(word):
                return True
            i,j=row,col
            ind=0
            while (j>=0 and i<n) and ind<len(word) and mat[i][j]==word[ind]:
                i+=1
                j-=1
                ind+=1
            if ind==len(word):
                return True
            i,j=row,col
            ind=0
            while (i>=0 and j<m) and ind<len(word) and mat[i][j]==word[ind]:
                i-=1
                j+=1
                ind+=1
            if ind==len(word):
                return True
            i,j=row,col
            ind=0
            while (i>=0 and j>=0) and ind<len(word) and mat[i][j]==word[ind]:
                i-=1
                j-=1
                ind+=1
            if ind==len(word):
                return True
            return False
        n,m=len(mat),len(mat[0])
        ans=[]
        for i in range(n):
            for j in range(m):
                if mat[i][j]==word[0] and check_all_directions(i,j):
                    ans.append((i,j))
        return ans
            