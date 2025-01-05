#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        n=len(arr)
        arr.sort()
        def binary_search(ele,start,arr):
            l,r=start,n-1
            ans=-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]<ele:
                    ans=mid
                    l=mid+1
                else:
                    r=mid-1
            return ans if ans!=-1 else start
        cnt=0
        for i in range(n):
            x=target-arr[i]
            cnt+=(binary_search(x,i,arr)-i)
        return cnt

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends