#User function Template for python3

class Solution:
    def countSubarrays(self, arr,n,L,R): 
        # Complete the function
        cnt=0
        tot=0
        less=0
        x=0
        for i in range(n):
            if arr[i]>=L and arr[i]<=R:
                tot+=(cnt+1+less)
                x=(cnt+1+less)
                cnt+=1
            elif arr[i]<L:
                tot+=x
                less+=1
            elif arr[i]>R:
                cnt=0
                less=0
                x=0
        return tot

#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    n,l,r = map(int, input().strip().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    v = ob.countSubarrays(arr, n, l, r)
    print(v)
    
# } Driver Code Ends