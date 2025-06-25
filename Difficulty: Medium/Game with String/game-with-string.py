import heapq
class Solution:
    def minValue(self, s, k):
        #code here
        chars=[0]*26
        n=len(s)
        for i in range(n):
            chars[ord(s[i])-97]+=1
        heap=[]
        for i in chars:
            if i>0:
                heapq.heappush(heap,-i)
        while heap and k>0:
            ele=-1*heapq.heappop(heap)
            ele-=1
            if ele>0:
                heapq.heappush(heap,-ele)
            k-=1
        tot=0
        while heap:
            tot+=(heapq.heappop(heap))**2
        return tot
        
        