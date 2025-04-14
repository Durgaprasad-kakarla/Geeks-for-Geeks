#User function Template for python3

class Solution:
    def bellmanFord(self, V, edges, src):
        #code here
        dist=[float('inf')]*V
        dist[src]=0
        for i in range(V-1):
            for u,v,wt in edges:
                if dist[u]+wt<dist[v]:
                    dist[v]=dist[u]+wt
        for u,v,wt in edges:
            if dist[u]+wt<dist[v]:
                return [-1]
        for i in range(V):
            if dist[i]==float('inf'):
                dist[i]=10**8
        return dist

#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        V = int(input())
        E = int(input())
        edges = []
        for i in range(E):
            u, v, w = map(int, input().strip().split())
            edges.append([u, v, w])
        S = int(input())
        ob = Solution()

        res = ob.bellmanFord(V, edges, S)
        for i in res:
            print(i, end=" ")
        print()
        print("~")

# } Driver Code Ends