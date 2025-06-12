import heapq
class Solution:
    def printKClosest(self, arr, k, x):
        # code here
        n=len(arr)
        heap=[]
        for i in range(n):
            heapq.heappush(heap,[abs(x-arr[i]),-arr[i]])
        closest=[]
        while heap and k>0:
            d,ele=heapq.heappop(heap)
            if x!=-1*ele:
                closest.append(-1*ele)
                k-=1
        return closest