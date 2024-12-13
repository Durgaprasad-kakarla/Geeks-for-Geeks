#User function Template for python3

class Solution:
    def search(self,arr,target):
        # Complete this function
        n=len(arr)
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==target:
                return mid
            if arr[l]<=arr[mid]:
                if arr[l]<=target and arr[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if arr[mid]<target and arr[r]>=target:
                    l=mid+1
                else:
                    r=mid-1
        return -1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        k = int(input())
        ob = Solution()
        print(ob.search(A, k))
        print("~")

# } Driver Code Ends