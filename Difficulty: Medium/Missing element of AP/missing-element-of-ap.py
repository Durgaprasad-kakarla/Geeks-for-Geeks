#User function Template for python3

class Solution:
    def findMissing(self, arr):
        # code here
        n=len(arr)
        mini,maxi=float('inf'),-float('inf')
        for i in range(1,n):
            mini=min(mini,arr[i]-arr[i-1])
            maxi=max(maxi,arr[i]-arr[i-1])
        if mini==maxi:
            return arr[n-1]+mini
        for i in range(1,n):
            if arr[i]-arr[i-1]==maxi:
                return arr[i-1]+mini


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys
import math


def main():
    input = sys.stdin.read
    data = input().strip().split('\n')

    t = int(data[0])
    solution = Solution()

    for i in range(1, t + 1):
        arr = list(map(int, data[i].split()))
        print(solution.findMissing(arr))
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends