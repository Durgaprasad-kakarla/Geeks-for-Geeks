#User function Template for python3

from typing import List
from collections import deque

class Solution:

    def shortestPath(self, V: int, E: int,edges: List[List[int]]) -> List[int]:
        adj=[[] for i in range(V)]
        for u,v,wt in edges:
            adj[u].append([v,wt])
        dist=[float('inf')]*n
        dist[0]=0
        queue=deque()
        queue.append([0,0])
        while queue:
            node,d=queue.popleft()
            for i,wt in adj[node]:
                if dist[i]>dist[node]+wt:
                    dist[i]=dist[node]+wt
                    queue.append([i,dist[i]])
        for i in range(V):
            if dist[i]==float('inf'):
                dist[i]=-1
        return dist



#{ 
 # Driver Code Starts
#Initial Template for Python 3

from typing import List


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


class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        m = int(input())
        edges = IntMatrix().Input(m, 3)
        obj = Solution()
        res = obj.shortestPath(n, m, edges)

        IntArray().Print(res)
        print("~")

# } Driver Code Ends