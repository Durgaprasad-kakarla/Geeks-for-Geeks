class Solution:
    def startStation(self, gas, cost):
        # Your code here
        gc = [g - c for g, c in zip(gas, cost)]
        
        start, running, n, cnt = -1, 0, len(gas), 0

        for i in range(2*n):
            e = gc[i%n]
            running += e
            if running < 0:
                running = 0
                start = -1
                cnt = 0
            else:
                if start == -1:
                    start = i
                cnt += 1
            if cnt == n:
                break
        return -1 if cnt != n else start
 


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import io
import sys

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        gas = list(map(int, input().strip().split()))
        cost = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.startStation(gas, cost)
        print(ans)
        print("~")

# } Driver Code Ends