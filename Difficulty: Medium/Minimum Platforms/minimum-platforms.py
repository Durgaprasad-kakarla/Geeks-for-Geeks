#User function Template for python3
import heapq
class Solution:    
    #Function to find the minimum number of platforms required at the
    #railway station such that no train waits.
    def minimumPlatform(self,arr,dep):
        # code here
        arr_dep=[]
        n=len(arr)
        for i in range(n):
            arr_dep.append([arr[i],dep[i]])
        arr_dep.sort()
        heap=[]
        maxi=0
        for i in range(n):
            while heap and arr_dep[i][0]>heap[0]:
                heapq.heappop(heap)
            heapq.heappush(heap,arr_dep[i][1])
            maxi=max(maxi,len(heap))
        return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        arrival = list(map(int, input().strip().split()))
        departure = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.minimumPlatform(arrival, departure))
        print("~")

# } Driver Code Ends