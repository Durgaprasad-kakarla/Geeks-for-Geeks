
#User function Template for python3


class Solution:
    
    #Function to return sum of upper and lower triangles of a matrix.
    def sumTriangles(self,matrix, n):
        # code here 
        upper,lower=0,0
        for i in range(n):
            for j in range(i+1):
                lower+=matrix[i][j]
        for i in range(n):
            for j in range(i,n):
                upper+=matrix[i][j]
        return upper,lower
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        matrix = [[0 for j in range(n)] for i in range(n)]
        line1 = [int(x) for x in input().strip().split()]

        k=0
        for i in range(n):
            for j in range (n):
                matrix[i][j]=line1[k]
                k+=1
        obj = Solution()
        ans = obj.sumTriangles(matrix, n)
        for i in ans:
            print(i,end=" ")
        print()
# } Driver Code Ends