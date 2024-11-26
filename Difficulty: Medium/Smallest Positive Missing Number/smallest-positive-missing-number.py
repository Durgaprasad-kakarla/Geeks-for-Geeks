#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        n=len(arr)
        arr.sort()
        res=1
        for i in range(n):
            if (arr[i]<=0) or (i>0 and arr[i-1]==arr[i]):
                continue
            if res==arr[i]:
                res+=1
            else:
                return res
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    T = int(input())
    while (T > 0):
        arr = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.missingNumber(arr))
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends