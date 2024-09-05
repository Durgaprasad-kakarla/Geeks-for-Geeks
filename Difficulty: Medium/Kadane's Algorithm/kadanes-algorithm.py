#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        n=len(arr)
        maxi,sm=-float('inf'),0
        f=0
        for i in range(n):
            sm+=arr[i]
            f=0
            if sm<0:
                f=1
                sm=0
            if f==0:
                maxi=max(maxi,sm)
        return maxi if maxi!=-float('inf') else max(arr)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.maxSubArraySum(arr))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends