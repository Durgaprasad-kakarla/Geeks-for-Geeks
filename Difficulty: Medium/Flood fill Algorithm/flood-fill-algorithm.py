from collections import deque
class Solution:
	def floodFill(self, image, sr, sc, newColor):
		#Code here
		n,m=len(image),len(image[0])
        queue=deque()
        queue.append([sr,sc])
        oldColor=image[sr][sc]
        vis=[[0 for _ in range(m)] for _ in range(n)]
        vis[sr][sc]=1
        while queue:
            row,col=queue.popleft()
            dr=[-1,0,1,0]
            dc=[0,-1,0,1]
            for i in range(4):
                nrow=row+dr[i]
                ncol=col+dc[i]
                if nrow>=0 and nrow<n and ncol>=0 and ncol<m and image[nrow][ncol]==oldColor and not vis[nrow][ncol]:
                    vis[nrow][ncol]=1
                    queue.append([nrow,ncol])
        for i in range(n):
            for j in range(m):
                if vis[i][j]:
                    image[i][j]=newColor
        return image

#{ 
 # Driver Code Starts
import sys

sys.setrecursionlimit(10**7)

T = int(input())  # Read number of test cases
for i in range(T):
    n = int(input())
    m = int(input())

    # Reading the image matrix
    image = []
    for _ in range(n):
        image.append(list(map(int, input().split())))

    # Read starting row, column, and new color
    sr = int(input())
    sc = int(input())
    newColor = int(input())

    # Create an instance of the Solution class and apply floodFill
    obj = Solution()
    ans = obj.floodFill(image, sr, sc, newColor)

    for row in ans:
        print(" ".join(map(str, row)))
    print("~")

# } Driver Code Ends