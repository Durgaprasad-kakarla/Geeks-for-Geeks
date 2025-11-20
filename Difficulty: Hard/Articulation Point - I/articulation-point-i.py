#User function Template for python3

import sys
sys.setrecursionlimit(10**6)

class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def articulationPoints(self, V, adj):
        # code here
        def dfs(node,parent):
            global timer
            vis[node]=1
            tin[node]=low[node]=timer
            timer+=1
            child=0
            for i in adj[node]:
                if i==parent:
                    continue
                if not vis[i]:
                    dfs(i,node)
                    low[node]=min(low[node],low[i])
                    if tin[node]<=low[i] and parent!=-1:
                        mark[node]=1
                    child+=1
                else:
                    low[node]=min(low[node],tin[i])
            # print(node,child)
            if child>1 and parent==-1:
                mark[node]=1
        global timer
        timer=0
        vis,tin,low,mark=[0]*V,[0]*V,[0]*V,[0]*V
        for i in range(V):
            if not vis[i]:
                dfs(i,-1)
        articulation_points=[]
        for i in range(V):
            if mark[i]:
                articulation_points.append(i)
        return articulation_points if articulation_points else [-1]