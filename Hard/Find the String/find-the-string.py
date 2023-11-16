#User function Template for python3

class Solution:
    def findString(self, N, K):
        # code here 
        seen=set()
        start="0"*(N-1)
        edges=[]
        def dfs(k,prev,seen,edges):
            for i in range(k):
                cur=prev
                cur+=str(i)
                if cur not in seen:
                    seen.add(cur)
                    dfs(k,cur[1:],seen,edges)
                    edges.append(i)
        dfs(K,start,seen,edges)
        ret=""
        l=K**N
        for i in range(l):
            ret+=str(edges[i])
        ret+=start
        return ret

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())

        ob = Solution()
        ans = ob.findString(N,K)
        ok = 1
        for i in ans:
            if ord(i)<48 or ord(i)>K-1+48:
                ok = 0
        if not ok:
            print(-1)
            continue
        d = dict()
        i = 0
        while i+N-1<len(ans):
            d[ans[i:i+N]] = 1
            i += 1
        tot = pow(K,N)
        if len(d)==tot:
            print(len(ans))
        else:
            print(-1)
# } Driver Code Ends