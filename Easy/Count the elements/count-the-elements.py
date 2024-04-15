#User function Template for python3
class Solution:
    def countElements(self, a, b, n, query, q):
        # code here
        def func(arr,x):
            l,r=0,len(arr)-1
            while l<=r:
                mid=(l+r)//2
                if arr[mid]<=x:
                    l=mid+1
                else:
                    r=mid-1
            return r+1
        b.sort()
        ans=[]
        for i in range(q):
            x=a[query[i]]
            ans.append(func(b,x))
        return ans
            
            
            
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = int(input())
    query = []
    ob = Solution()
    for i in range(q):
        query.append(int(input()))
    ans = ob.countElements(a, b, n, query, q)
    for i in range(q):
        print(ans[i])

# } Driver Code Ends