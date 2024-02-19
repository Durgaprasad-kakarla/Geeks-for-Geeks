#User function Template for python3
import heapq
class Solution:
    def minValue(self, s, k):
        # code here
        n=len(s)
        heap=[]
        dic={}
        for i in range(n):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
        for i in dic:
            heapq.heappush(heap,-dic[i])
        while k>0:
            x=heapq.heappop(heap)
            if x+1<0:
                heapq.heappush(heap,x+1)
            k-=1
        sm=0
        for i in heap:
            sm+=abs(i)*abs(i)
        return sm


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends