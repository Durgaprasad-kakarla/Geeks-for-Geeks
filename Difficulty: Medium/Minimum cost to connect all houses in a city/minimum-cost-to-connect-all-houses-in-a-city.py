#User function Template for python3
class disjointset:
    def __init__(self,n):
        self.rank=[0]*(n+1)
        self.par=list(range(n+1))
    def findupar(self,node):
        if self.par[node]==node:
            return node
        self.par[node]=self.findupar(self.par[node])
        return self.par[node]
    def union_by_rank(self,u,v):
        ulp_u=self.findupar(u)
        ulp_v=self.findupar(v)
        if ulp_v==ulp_u:
            return
        if self.rank[ulp_u]<self.rank[ulp_v]:
            self.par[ulp_u]=ulp_v
        elif self.rank[ulp_u]>self.rank[ulp_v]:
            self.par[ulp_v]=ulp_u
        else:
            self.par[ulp_v]=ulp_u
            self.rank[ulp_u]+=1
import heapq
class Solution:
    def minCost(self, houses):
        n=len(houses)
        def distance(x1,x2,y1,y2):
            return abs(x1-x2)+abs(y1-y2)
        vis=[0]*n
        heap=[]
        for i in range(n):
            for j in range(n):
                if i!=j:
                    x1,y1=houses[i]
                    x2,y2=houses[j]
                    heapq.heappush(heap,[distance(x1,x2,y1,y2),i,j])
        ds=disjointset(n)
        cost,cnt=0,0
        while heap and cnt<n-1:
            d,node1,node2=heapq.heappop(heap)
            u,v=ds.findupar(node1),ds.findupar(node2)
            if u!=v:
                ds.union_by_rank(u,v)
                cnt+=1
                cost+=d
        return cost

#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        edges = []

        for _ in range(n):
            temp = list(map(int, input().split()))
            edges.append(temp)

        obj = Solution()
        print(obj.minCost(edges))
        print("~")
# } Driver Code Ends