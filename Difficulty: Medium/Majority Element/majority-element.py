#User function template for Python 3

class Solution:
    def majorityElement(self, arr):
        #code here
        n=len(arr)
        ele,cnt=-1,0
        for i in range(n):
            if cnt==0:
                ele=arr[i]
                cnt+=1
            elif ele==arr[i]:
                cnt+=1
            else:
                cnt-=1
        cnt=0
        for i in range(n):
            if ele==arr[i]:
                cnt+=1
        if cnt>(n//2):
            return ele
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
from sys import stdin


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]

        obj = Solution()
        print(obj.majorityElement(arr))
        print("~")
        t -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends