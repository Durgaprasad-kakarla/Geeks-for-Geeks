#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        def isSafe(board, row, col, n):
            # checking the upper elements of that column
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            # checking the upper left diagonal
            for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
                if board[i][j] == 'Q':
                    return False
            #checking the upper right diagonal
            for i, j in zip(range(row, -1, -1), range(col, n, 1)):
                if board[i][j] == 'Q':
                    return False
            return True


        def NQutil(board, row, n):
            if row >= n:
                printsolution(board, n)
                return
            for i in range(n):
                if isSafe(board, row, i, n):
                    board[row][i] = 'Q'
                    if NQutil(board, row + 1, n):
                        return True
                    board[row][i] = '.'
            return False
        list2=[]
        def printsolution(board, n):
            list1=[]
            for i in board:
                s=''
                for j in i:
                    s=s+j
                list1.append(s)
            list2.append(list1)
        board = [['.'for i in range(n)]for j in range(n)]
        NQutil(board,0,n)
        final=[]
        for lst in list2:
            l=[]
            for s in lst:
                for i in range(len(s)):
                    if s[i]=='Q':
                        l.append(i+1)
            final.append(l)
        return final


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        ans = ob.nQueen(n)
        if (len(ans) == 0):
            print("-1")
        else:
            ans.sort()
            for i in range(len(ans)):
                print("[", end="")
                for j in range(len(ans[i])):
                    print(ans[i][j], end=" ")
                print("]", end=" ")
            print()

        print("~")

# } Driver Code Ends