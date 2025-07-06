from heapq import heappop,heappush
class Solution:
    def topKSumPairs(self, a, b, k):
        # code here
        n,m=len(a),len(b)
        a.sort(reverse=True)
        b.sort(reverse=True)
        vis=set()
        vis.add((0,0))
        heap=[]
        heappush(heap,[-(a[0]+b[0]),0,0])
        ans=[]
        while heap and k>0:
            sm,ind1,ind2=heappop(heap)
            ans.append(sm*-1)
            if ind1+1<n and (ind1+1,ind2) not in vis:
                heappush(heap,[-(a[ind1+1]+b[ind2]),ind1+1,ind2])
                vis.add((ind1+1,ind2))
            if ind2+1<n and (ind1,ind2+1) not in vis:
                heappush(heap,[-(a[ind1]+b[ind2+1]),ind1,ind2+1])
                vis.add((ind1,ind2+1))
            k-=1
        return ans