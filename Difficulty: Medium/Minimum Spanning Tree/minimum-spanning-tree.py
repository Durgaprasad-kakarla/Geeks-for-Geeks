#User function Template for python3
from typing import List
import heapq
class Solution:
    
    #Function to find sum of weights of edges of the Minimum Spanning Tree.
    def spanningTree(self, V: int, adj: List[List[int]]) -> int:
        #code here
        heap=[]
        heapq.heappush(heap,[0,0])
        vis=[0]*V
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

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys
from typing import List

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V = int(input())
        E = int(input())
        adj = [[] for i in range(V)]
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            adj[u].append([v, w])
            adj[v].append([u, w])
        ob = Solution()

        print(ob.spanningTree(V, adj))
        print("~")

# } Driver Code Ends