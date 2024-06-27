# You are required to complete this method
# Return True/False or 1/0
def isToepliz(mat):
    #code here
    n,m=len(mat),len(mat[0])
    i=0
    for j in range(m):
        l,r,prev=i,j,-1
        while l<n and r<m:
            if prev==-1:
                prev=mat[l][r]
            elif prev!=mat[l][r]:
                return 0
            l+=1
            r+=1
    j=0
    for i in range(1,n):
        l,r,prev=i,0,-1
        while l<n and r<m:
            if prev==-1:
                prev=mat[l][r]
            elif prev!=mat[l][r]:
                return 0
            l+=1
            r+=1
    return 1


#{ 
 # Driver Code Starts
# Your code goes here
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n, m = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(m)] for j in range(n)]
        k = 0
        for i in range(n):
            for j in range(m):
                matrix[i][j] = arr[k]
                k += 1
        b = isToepliz(matrix)

        if n == 2 and m == 4:
            print(0)
        else:
            if b == True:
                print("true")
            else:
                print("false")

# } Driver Code Ends