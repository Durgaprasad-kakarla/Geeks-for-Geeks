#User function Template for python3
class Solution:

	def count(self,arr, n, x):
		# code here
        def lower_bound(arr,target):
            n=len(arr)
            l,r,ans=0,n-1,-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]==target:
                    ans=mid
                    r=mid-1
                elif arr[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return ans
        def upper_bound(arr,target):
            n=len(arr)
            l,r,ans=0,n-1,-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]==target:
                    ans=mid
                    l=mid+1
                elif arr[mid]>target:
                    r=mid-1
                else:
                    l=mid+1
            return ans
        lower,upper=lower_bound(arr,x),upper_bound(arr,x)
        if lower==-1:
            return 0
        return upper-lower+1

#{ 
 # Driver Code Starts
#Initial Template for Python 3




if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, x = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.count(arr, n, x)
        print(ans)
        tc -= 1

# } Driver Code Ends