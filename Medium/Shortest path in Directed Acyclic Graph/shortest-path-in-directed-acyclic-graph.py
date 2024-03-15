#User function Template for python3

from typing import List

class Solution:
    def shortestPath(self, n : int, m : int, edges : List[List[int]]) -> List[int]:
        adj=[[] for i in range(n)]
        for u,v,wt in edges:
            adj[u].append([v,wt])
    
        def dfs(node,vis,stack):
            vis[node]=1
            for i,wt in adj[node]:
                if not vis[i]:
                    dfs(i,vis,stack)
            stack.append(node)
        vis=[0 for i in range(n)]
        stack=[]
        for i in range(n):
            if not vis[i]:
                dfs(i,vis,stack)
        dist=[float('inf') for i in range(n)]
        dist[0]=0
        while stack:
            node=stack.pop()
            for u,wt in adj[node]:
                if dist[node]+wt<dist[u]:
                    dist[u]=dist[node]+wt
        for i in range(n):
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
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()



class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n,m=map(int,input().split())
        
        
        edges=IntMatrix().Input(m, 3)
        
        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        
        IntArray().Print(res)
# } Driver Code Ends