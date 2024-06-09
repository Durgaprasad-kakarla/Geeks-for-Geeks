#User function Template for python3
class Solution:
    def findKRotation(self,arr,  n):
        # code here
        n=len(arr)
        l,r=0,n-1
        mini=float('inf')
        while l<=r:
            mid=(l+r)//2
            if mini>arr[mid]:
                mini=arr[mid]
                index=mid
            if arr[l]<=arr[mid]:
                if arr[mid]<=arr[r]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if arr[mid]<=arr[r]:
                    r=mid-1
                else:
                    l=mid+1
        return index


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	tc=int(input())
	while tc > 0:
		n=int(input())
		a=list(map(int , input().strip().split()))
		ob = Solution()
		ans=ob.findKRotation(a, n)
		print(ans)
		tc=tc-1



# } Driver Code Ends