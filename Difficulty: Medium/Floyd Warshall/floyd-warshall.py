#User function template for Python

class Solution:
	def floydWarshall(self, matrix):
		#Code here
        n=len(matrix)
        for i in range(n):
            for j in range(n):
                if matrix[i][j]==10**8:
                    matrix[i][j]=float("inf")
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    matrix[i][j]=min(matrix[i][j],matrix[i][via]+matrix[via][j])
        for i in range(n):
            for j in range(n):
                if matrix[i][j]==float('inf'):
                    matrix[i][j]=10**8
        return matrix

#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        matrix = []
        for _ in range(n):
            matrix.append(list(map(int, input().split())))
        obj = Solution()
        obj.floydWarshall(matrix)
        for _ in range(n):
            for __ in range(n):
                print(matrix[_][__], end=" ")
            print()
        print("~")

# } Driver Code Ends