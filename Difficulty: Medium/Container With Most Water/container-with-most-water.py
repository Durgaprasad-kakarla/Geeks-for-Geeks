
class Solution:
    def maxWater(self, arr):
        # code here
        n=len(arr)
        l,r=0,n-1
        maxi=0
        while l<r:
            maxi=max(maxi,min(arr[l],arr[r])*(r-l))
            if arr[l]<=arr[r]:
                l+=1
            else:
                r-=1
        return maxi
        # stack=[]
        # for i in range(n):
        #     print(i,stack,maxi)
        #     while stack and stack[-1][0]>=arr[i]:
        #         ele,ind=stack.pop()
        #         maxi=max(maxi,(i-ind)*arr[i])
        #     stack.append([arr[i],i])
        #     maxi=max(maxi,(i-stack[0][1])*stack[0][0])
        # return maxi


#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends