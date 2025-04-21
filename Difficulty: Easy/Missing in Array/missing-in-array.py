class Solution:
    def missingNum(self, arr):
        # code here
        n=len(arr)
        extra=-1
        for i in range(n):
            if arr[i]>n:
                extra=arr[i]
        if extra!=-1:
            k=sum(arr)-extra
            return (n*(n+1))//2-k
        return n+1
#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    arr = list(map(int, input().split()))
    s = Solution().missingNum(arr)
    print(s)

    print("~")
# } Driver Code Ends