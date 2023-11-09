class Solution:
    def transitionPoint(self, arr, n): 
        # Code here
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==1:
                if mid==0:
                    return mid
                elif mid>0 and arr[mid-1]==0:
                        return mid
                elif mid>0 and arr[mid-1]==1:
                        r=mid-1
            else:
                if mid==0:
                    return -1
                if mid>0 and arr[mid-1]==0:
                    l=mid+1
                elif mid<n-1 and arr[mid+1]==1:
                    return mid+1
        return -1
#{ 
 # Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.transitionPoint(arr, n))

# } Driver Code Ends