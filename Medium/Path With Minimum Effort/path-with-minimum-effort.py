
from typing import List
import heapq


class Solution:
    def MinimumEffort(self, rows : int, columns : int, heights : List[List[int]]) -> int:
        # code here
        n,m=rows,columns
        heap=[]
        heapq.heappush(heap,[0,0,0])
        dist=[[float('inf') for i in range(m)] for j in range(n)]
        dist[0][0]=0
        while heap:
            diff,row,col=heapq.heappop(heap)
            if row==n-1 and col==m-1:
                return diff
            dr=[0,-1,0,1]
            dc=[-1,0,1,0]
            for i in range(4):
                nrow=row+dr[i]
                ncol=col+dc[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m:
                    maxi=max(diff,abs(heights[nrow][ncol]-heights[row][col]))
                    if maxi<dist[nrow][ncol]:
                        dist[nrow][ncol]=maxi
                        heapq.heappush(heap,[maxi,nrow,ncol])
        return -1
            



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

        rows = int(input())

        columns = int(input())

        heights = IntMatrix().Input(rows, columns)

        obj = Solution()
        res = obj.MinimumEffort(rows, columns, heights)

        print(res)

# } Driver Code Ends