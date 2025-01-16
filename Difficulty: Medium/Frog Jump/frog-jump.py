#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys


# } Driver Code Ends
#User function Template for python3
class Solution:
    def minCost(self, height):
        # code here
        n=len(height)
        def func(ind):
            if ind==0:
                return 0
            if dp[ind]!=-1:
                return dp[ind]
            l=abs(height[ind]-height[ind-1])+func(ind-1)
            r=float('inf')
            if ind>1:
                r=abs(height[ind]-height[ind-2])+func(ind-2)
            dp[ind]=min(l,r)
            return min(l,r)
        dp=[-1 for i in range(n)]
        return func(n-1)

#{ 
 # Driver Code Starts.

if __name__ == "__main__":
    input_lines = sys.stdin.read().splitlines()
    
    pointer = 0
    
    t = int(input_lines[pointer].strip())
    pointer += 1
    
    for _ in range(t):
        arr = list(map(int, input_lines[pointer].strip().split()))
        pointer += 1
        
        ob = Solution()
        print(ob.minCost(arr))
        print("~")

# } Driver Code Ends