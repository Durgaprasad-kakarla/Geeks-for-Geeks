#User function Template for python3
import heapq
from typing import List
class Solution:
    def shortestPath(self,n:int, m:int, edges:List[List[int]] )->List[int]:
        # code here
        adj=[[] for i in range(n+1)]
        for u,v,w in edges:
            adj[u].append([v,w])
            adj[v].append([u,w])
        heap=[]
        heapq.heappush(heap,[0,1])
        dist=[float('inf') for i in range(n+1)]
        dist[1]=0
        prev=[-1 for i in range(n+1)]
        prev[1]=1
        flag=0
        while heap:
            d,node=heapq.heappop(heap)
            if node==n:
                flag=1
                break
            for i,wt in adj[node]:
                if dist[node]+wt<dist[i]:
                    dist[i]=dist[node]+wt
                    prev[i]=node
                    heapq.heappush(heap,[dist[i],i])
        if flag==0:
            return [-1]
        path=[]
        node=n
        while prev[node]!=node:
            path.append(node)
            node=prev[node]
        path=path+[1]
        path=[dist[n]]+path[::-1]
        return path
        


#{ 
 # Driver Code Starts
from collections import defaultdict


def check(n, path, edges):
    gp = [{} for i in range(n + 1)]
    for u, v, w in edges:
        if v in gp[u]:
            gp[u][v] = min(gp[u][v], w)
        else:
            gp[u][v] = w

        if u in gp[v]:
            gp[v][u] = min(gp[v][u], w)
        else:
            gp[v][u] = w

    s = 0
    for i in range(2, len(path)):
        if path[i] not in gp[path[i - 1]]:
            return False
        s += gp[path[i - 1]][path[i]]

    return s == path[0]


if __name__ == "__main__":
    for _ in range(int(input())):
        n, m = map(int, input().split())
        edges = []
        for i in range(m):
            a, b, w = map(int, input().split())
            edges.append([a, b, w])

        obj = Solution()
        res = obj.shortestPath(n, m, edges)
        if res[0] == -1:
            print(-1)
        else:
            if check(n, res, edges):
                print(res[0])
            else:
                print(-2)

# } Driver Code Ends