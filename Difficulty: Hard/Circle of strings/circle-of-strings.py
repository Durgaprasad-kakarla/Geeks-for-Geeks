#User function Template for python3
from collections import deque,Counter,defaultdict
class Solution:
    def isCircle(self, arr):
        # code here
        n=len(arr)
        dic=defaultdict(list)
        indegree,outdegree=Counter(),Counter()
        for s in arr:
            dic[s[0]].append(s[-1])
            indegree[s[-1]]+=1
            outdegree[s[0]]+=1
        if indegree!=outdegree:
            return 0
        vis=set()
        def dfs(node,dic):
            if node in vis:
                return 
            vis.add(node)
            for i in dic[node]:
                dfs(i,dic)
        dfs(arr[0][0],dic)
        if len(vis)!=len(dic):
            return 0
        return 1
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        A = input().split()

        ob = Solution()
        print(ob.isCircle(A))

# } Driver Code Ends