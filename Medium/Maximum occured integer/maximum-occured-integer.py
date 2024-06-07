#User function Template for python3
from collections import Counter
class Solution:
    #Complete this function
    #Function to find the maximum occurred integer in all ranges.
    def maxOccured(self,n, l, r, maxx):
        ##Your code here
        pref=[0]*(maxx+1)
        for i in range(n):
            start=l[i]-1
            end=r[i]-1
            pref[start]+=1
            pref[end+1]+=-1
        maxi=0
        index=-1
        for i in range(1,maxx+1):
            pref[i]=pref[i-1]+pref[i]
            if maxi<pref[i]:
                maxi=pref[i]
                index=i+1
        return index
            
            
            
            
            
            
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

A = [0] * 1000000


def main():

    T = int(input())

    while (T > 0):

        global A
        A = [0] * 1000000

        n = int(input())

        l = [int(x) for x in input().strip().split()]
        r = [int(x) for x in input().strip().split()]

        maxx = max(r)
        ob = Solution()
        print(ob.maxOccured(n, l, r, maxx))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends