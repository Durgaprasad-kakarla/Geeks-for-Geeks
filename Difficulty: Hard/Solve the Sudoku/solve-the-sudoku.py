#User function Template for python3

class Solution:
    
    #Function to find a solved Sudoku. 
    def solveSudoku(self, board):
        
        # Your code here
        def solve(row,col,board):
            if row==9:
                return True
            if col==9:
                return solve(row+1,0,board)
            if board[row][col]==0:
                for ch in range(1,10):
                    if issafe(row,col,ch):
                        board[row][col]=ch
                        if solve(row,col+1,board):
                            return True
                        else:   
                            board[row][col]=0
                return False
            else:
                return solve(row,col+1,board)
        def issafe(row,col,ele):
            for i in range(9):
                if board[i][col]==ele:
                    return False
            for i  in range(9):
                if board[row][i]==ele:
                    return False
            for i in range(9):
                if board[3*(row//3)+(i//3)][3*(col//3)+(i%3)]==ele:
                    return False
            return True
        solve(0,0,board)
        return board
                                
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    for _ in range(t):
        matrix = []
        n = 9
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            matrix.append(row)
            index += n
        obj = Solution()
        obj.solveSudoku(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()
        print("~")

# } Driver Code Ends