#User function Template for python3

class Solution:
    def antiDiagonalPattern(self,mat):
        # Code here
        i,j=0,0
        n=len(mat)
        m=len(mat[0])
        new_mat=[]
        for x in range(n):
            lst=[]
            while i>=0 and j<m and i<n and j>=0:
                lst.append(mat[i][j])
                i-=1
                j+=1
            i,j=x+1,0
            new_mat.append(lst)
        i=n-1
        j=1
        for x in range(1,m):
            lst=[]
            while i>=0 and i<n and j<m and j>=0:
                lst.append(mat[i][j])
                i-=1
                j+=1
            i=n-1
            j=x+1
            new_mat.append(lst)
        final=[]
        for i in range(len(new_mat)):
            final+=new_mat[i][::-1]
        return final

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input()) 
        inp=list(map(int,input().split()))
        matrix=[]
        k = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(inp[k])
                k += 1
            matrix.append(row)
        ob = Solution()
        ans = ob.antiDiagonalPattern(matrix)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends