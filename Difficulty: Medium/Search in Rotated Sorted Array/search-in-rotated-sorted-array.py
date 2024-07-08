#User function Template for python3

class Solution:
    def search(self,arr,key):
        # Complete this function
        l,r=0,len(arr)-1
        while l<=r:
            mid=(l+r)//2
            if arr[mid]==key:
                return mid
            if arr[l]<=arr[mid]:
                if arr[l]<=key and arr[mid]>key:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if arr[mid]<key and arr[r]>=key:
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

# } Driver Code Ends