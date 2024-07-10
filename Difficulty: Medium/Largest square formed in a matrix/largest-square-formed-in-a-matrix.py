
from typing import List


class Solution:
    def maxSquare(self, n : int, m : int, mat : List[List[int]]) -> int:
        # code here
        dp=[[0 for i in range(m)] for j in range(n)]
        maxi=0
        for i in range(m):
            dp[0][i]=mat[0][i]
            maxi=max(maxi,dp[0][i])
        for i in range(n):
            dp[i][0]=mat[i][0]
            maxi=max(maxi,dp[i][0])
        for i in range(1,n):
            for j in range(1,m):
                if mat[i][j]!=0:
                    if dp[i-1][j]==0 or dp[i][j-1]==0 or dp[i-1][j-1]==0:
                        dp[i][j]=1
                    elif dp[i-1][j]==dp[i][j-1] and dp[i-1][j]==dp[i-1][j-1]:
                        dp[i][j]=dp[i-1][j]+1
                    else:
                        dp[i][j]=min(dp[i-1][j],dp[i][j-1],dp[i-1][j-1])+1
                    maxi=max(maxi,dp[i][j])
        # print(dp)
        return maxi
                        



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n, m = map(int, input().split())

        mat = IntMatrix().Input(n, m)

        obj = Solution()
        res = obj.maxSquare(n, m, mat)

        print(res)

# } Driver Code Ends