class Solution:
    def maxLen(self, arr):
        # code here
        n=len(arr)
        for i in range(n):
            if arr[i]==0:
                arr[i]=-1
        dic,pref,maxi={0:-1},0,0
        for i in range(n):
            pref+=arr[i]
            if pref in dic:
                maxi=max(maxi,i-dic[pref])
            if pref not in dic:
                dic[pref]=i
        return maxi

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    a = list(map(int, input().split()))
    s = Solution().maxLen(a)
    print(s)

# } Driver Code Ends