#User function Template for python3

def rotate(mat): 
    #code here
    n,m=len(mat),len(mat[0])
    for i in range(n//2):
        mat[i],mat[n-i-1]=mat[n-i-1],mat[i]
    for i in range(n):
        for j in range(m):
            if i<j:
                mat[i][j],mat[j][i]=mat[j][i],mat[i][j]
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        matrix = []
        for i in range(N):
            arr = [int(x) for x in input().strip().split()]
            matrix.append(arr)

        rotate(matrix)
        for i in range(N):
            for j in range(N):
                print(matrix[i][j], end=' ')
            print()
        print("~")

# } Driver Code Ends