# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        n=len(arr)
        pref=[0]*n
        pref[0]=arr[0]
        for i in range(1,n):
            pref[i]+=pref[i-1]+arr[i]
        if pref[-1]-pref[1]==0:
            return 0
        for i in range(1,n-1):
            if pref[i-1]==pref[-1]-pref[i]:
                return i
        return -1




#{ 
 # Driver Code Starts
#Initial Template for Python 3
import math


def main():
    T = int(input())
    while (T > 0):

        arr = [int(x) for x in input().strip().split()]

        ob = Solution()

        print(ob.findEquilibrium(arr))
        print("~")
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends