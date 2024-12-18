class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self, arr, k):
        #code here
        n=len(arr)
        if k>n:
            return -1
        def max_pages(arr,x):
            sm,n=0,len(arr)
            cnt=0
            for i in range(n):
                sm+=arr[i]
                if sm>x:
                    cnt+=1
                    sm=arr[i]
            if sm>0:
                cnt+=1
            return cnt
        l,r=max(arr),sum(arr)
        while l<=r:
            mid=(l+r)//2
            if max_pages(arr,mid)>k:
                l=mid+1
            else:
                r=mid-1
        return l



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
        ans = ob.findPages(A, D)
        print(ans)
        print("~")

# } Driver Code Ends