#User function Template for python3
import heapq
class Solution:
    def minCost(self, houses):
      # code here
        n=len(houses)
        edges=[]
        for i in range(n):
            for j in range(i,n):
                diff=abs(houses[i][0]-houses[j][0])+abs(houses[i][1]-houses[j][1])
                edges.append([i,j,diff])
        adj=[[] for _ in range(n)]
        for u,v,wt in edges:
            adj[u].append([v,wt])
            adj[v].append([u,wt])
        heap=[]
        heapq.heappush(heap,[0,0])
        vis=[0]*n
        tot=0
        while heap:
            d,node=heapq.heappop(heap)
            if vis[node]:
                continue
            tot+=d
            vis[node]=1
            for i,wt in adj[node]:
                if not vis[i]:
                    heapq.heappush(heap,[wt,i])
        return tot
            
    