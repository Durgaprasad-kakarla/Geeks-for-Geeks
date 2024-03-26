#User function Template for python3

from typing import List
from collections import defaultdict
import heapq
import sys
class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        #Your code here
        dist=[float('inf')]*n 
        adj=[[] for i in range(n)]
        for u,v,wt in edges:
            adj[u].append([v,wt])
            adj[v].append([u,wt])
        heap=[]
        heapq.heappush(heap,[0,0])
        dist[0]=0
        ways=[0]*n
        ways[0]=1
        while heap:
            d,node=heapq.heappop(heap)
            for i,wt in adj[node]:
                if wt+dist[node]<dist[i]:
                    dist[i]=wt+dist[node]
                    ways[i]=ways[node]
                    heapq.heappush(heap,[dist[i],i])
                elif wt+dist[node]==dist[i]:
                    ways[i]+=ways[node]
        return ways[n-1]%(10**9+7)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

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
        
        
        adj=[]
        
        for i in range(m):
            tmp =[]
            x,y,z=map(int,input().split())
            tmp.append(x)
            tmp.append(y)
            tmp.append(z)
            adj.append(tmp)
            
        
        
        
       
        obj = Solution()
        res = obj.countPaths(n, adj)
        
        print(res)
        

# } Driver Code Ends