#User function Template for python3

class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,tot_wt, wt, val, n):
        prev=[0 for i in range(tot_wt+1)]
        for i in range(wt[0],tot_wt+1):
            prev[i]=val[0]
        n=len(wt)
        for i in range(1,n):
            cur=[0 for i in range(tot_wt+1)]
            for j in range(tot_wt,-1,-1):
                l=prev[j]
                r=sys.maxsize*-1
                if wt[i]<=j:
                    r=val[i]+prev[j-wt[i]]
                cur[j]=max(l,r)
            prev=cur
        return prev[tot_wt]


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        W = int(input())
        val = list(map(int,input().strip().split()))
        wt = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.knapSack(W,wt,val,n))
# } Driver Code Ends