# Your task is to complete this function
# Finction should return Integer
class Solution:
    def sequenceCount(self,s, t):
        # Code here
        n,m=len(s),len(t)
        prev=[0]*(m+1)
        prev[0]=1
        for ind1 in range(1,n+1):
            for ind2 in range(m,0,-1):
                if s[ind1-1]==t[ind2-1]:
                    prev[ind2]=prev[ind2-1]+prev[ind2]
        return prev[m]%(10**9+7)

#{ 
 # Driver Code Starts
#Initial template for Python 3

import sys
sys.setrecursionlimit(10**6)

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        arr = input().strip().split()
        print(Solution().sequenceCount(str(arr[0]), str(arr[1])))
# } Driver Code Ends