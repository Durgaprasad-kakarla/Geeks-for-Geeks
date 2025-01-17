#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        n=len(arr)
        suff=[0]*n
        suff[n-1]=arr[n-1]
        for i in range(n-2,-1,-1):
            suff[i]=suff[i+1]*arr[i]
        res=[0]*n
        res[0],pref=suff[1],arr[0]
        for i in range(1,n-1):
            res[i]=suff[i+1]*pref
            pref=pref*arr[i]
        res[n-1]=pref
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):

        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)
        print("~")

# } Driver Code Ends