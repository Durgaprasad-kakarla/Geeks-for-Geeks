import heapq
class Solution:
    def kSmallestPair(self, arr1, arr2, k):
        # code here
        heap=[]
        heapq.heappush(heap,[arr1[0]+arr2[0],0,0])
        n,m=len(arr1),len(arr2)
        sum_pairs=[]
        vis=set()
        vis.add((0,0))
        while heap and k>0:
            sm,i,j=heapq.heappop(heap)
            sum_pairs.append([arr1[i],arr2[j]])
            if i+1<n and (i+1,j) not in vis:
                heapq.heappush(heap,[arr1[i+1]+arr2[j],i+1,j])
                vis.add((i+1,j))
            if j+1<m and (i,j+1) not in vis:
                heapq.heappush(heap,[arr1[i]+arr2[j+1],i,j+1])
                vis.add((i,j+1))
            k-=1
        return sum_pairs
        