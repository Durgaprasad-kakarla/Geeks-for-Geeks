#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def solve(self, bt):
        # Code here
        sm=0
        bt.sort()
        n=len(bt)
        pref=bt[0]
        for i in range(1,n):
            sm+=pref
            pref+=bt[i]
        return sm//n

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        n = int(input())
        bt = list(map(int, input().split()))
        ob = Solution()
        res = ob.solve(bt)
        print(res)
        print("~")
# } Driver Code Ends