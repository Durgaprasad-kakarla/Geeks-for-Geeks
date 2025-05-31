from heapq import heappush,heappop
class Solution:
    def kthSmallest(self, matrix, k):
        # code here
        n,m=len(matrix),len(matrix[0])
        heap=[]
        for i in range(n):
            heappush(heap,[matrix[i][0],i,0])
        while heap and k>0:
            ele,row,col=heappop(heap)
            k-=1
            if col+1>=n:
                continue
            heappush(heap,[matrix[row][col+1],row,col+1])
        return ele