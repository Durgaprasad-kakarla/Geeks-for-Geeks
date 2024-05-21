#User function Template for python3
import heapq
class Solution:
    def printKClosest(self, arr, n, k, x):
        # code here
        heap=[]
        for i in range(n):
            heapq.heappush(heap,[abs(arr[i]-x),-arr[i]])
        closest=[]
        while k>0 and heap:
            d,ele=heapq.heappop(heap)
            if d==0:
                continue
            closest.append(-ele)
            k-=1
        return closest

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        k, x = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.printKClosest(arr, n, k, x)
        for xx in ans:
            print(xx, end=" ")
        print()
        tc -= 1

# } Driver Code Ends