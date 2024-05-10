#User function Template for python3

class Solution:
    
    def CombinationSum2(self, arr, n, k):
        # code here
        arr.sort()
        def func(ind,target,temp,ans):
            if target==0:
                ans.append(temp.copy())
                return 
            if ind==n:
                return 
            for i in range(ind,n):
                if i>ind and arr[i]==arr[i-1]:
                    continue
                if target<arr[i]:
                    break
                func(i+1,target-arr[i],temp+[arr[i]],ans)
        ans=[]
        func(0,k,[],ans)
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    ob = Solution()
    result = ob.CombinationSum2(arr, n, k)
    for row in result:
        print(*row)
    if not result:
        print()

# } Driver Code Ends