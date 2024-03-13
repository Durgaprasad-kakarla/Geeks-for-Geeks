# Your task is to complete this function

class Solution:
    def matrixDiagonally(self,mat):
        # code here
        n=len(mat)
        final=[]
        l=0
        for i in range(n):
            x=0
            y=i
            lst=[]
            while x>=0 and x<n and y>=0 and y<n:
                lst.append(mat[x][y])
                x+=1
                y-=1
            if l%2==0:
                final+=lst[::-1]
            else:
                final+=lst
            l+=1
        for i in range(1,n):
            x=i
            y=n-1
            lst=[]
            while x>=0 and x<n and y>=0 and y<n:
                lst.append(mat[x][y])
                x+=1
                y-=1
            if l%2==0:
                final+=lst[::-1]
            else:
                final+=lst
            l+=1
        return final
            
        


#{ 
 # Driver Code Starts
# Driver Program
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        matrix = [[0 for i in range(n[0])]for j in range(n[0])]
        k=0
        for i in range(n[0]):
            for j in range(n[0]):
                matrix[i][j] = arr[k]
                k+=1
        a = Solution().matrixDiagonally(matrix)
        for x in a:
            print(x,end=' ')
        print('')
# Contributed by: Harshit Sidhwa
# } Driver Code Ends