#User function Template for python3


class Solution:

    def aggressiveCows(self, stalls, k):
        def max_minDistance(arr,x):
            cnt,n=1,len(arr)
            ele=arr[0]
            for i in range(1,n):
                if arr[i]-ele>=x:
                    cnt+=1
                    ele=arr[i]
            return cnt
        stalls.sort()
        l,r=0,stalls[-1]-stalls[0]
        while l<=r:
            mid=(l+r)//2
            if max_minDistance(stalls,mid)<k:
                r=mid-1
            else:
                l=mid+1
        return r
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import bisect
#Main
if __name__ == '__main__':
    t = int(input())
    while t:
        t -= 1
        A = [int(x) for x in input().strip().split()]
        nd = [int(x) for x in input().strip().split()]
        D = nd[0]
        ob = Solution()
        ans = ob.aggressiveCows(A, D)
        print(ans)
        print("~")
# } Driver Code Ends