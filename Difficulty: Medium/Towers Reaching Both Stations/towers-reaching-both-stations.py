from collections import deque
class Solution:
    def countCoordinates(self, mat):
        # code here
        n,m=len(mat),len(mat[0])
        p_queue=deque()
        q_queue=deque()
        for i in range(n):
            p_queue.append((i,0))
            q_queue.append((i,m-1))
        for i in range(m):
            p_queue.append((0,i))
            q_queue.append((n-1,i))
        def func(queue,vis):
            while queue:
                row,col=queue.popleft()
                if (row,col) in vis:
                    continue
                vis.add((row,col))
                dr=[-1,0,1,0]
                dc=[0,-1,0,1]
                for i in range(4):
                    nrow=row+dr[i]
                    ncol=col+dc[i]
                    if nrow>=0 and nrow<n and ncol>=0 and ncol<m and mat[nrow][ncol]>=mat[row][col]:
                        queue.append((nrow,ncol))
            return vis
        p=func(p_queue,set())
        q=func(q_queue,set())
        return len(p.intersection(q))