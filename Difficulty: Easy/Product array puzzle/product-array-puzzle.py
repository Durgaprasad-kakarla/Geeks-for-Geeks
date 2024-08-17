#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        n=len(nums)
        if n==1:
            return [1]
        suff=[0]*(n)
        suff[n-1]=nums[n-1]
        for i in range(n-2,-1,-1):
            suff[i]=nums[i]*suff[i+1]
        pref=nums[0]
        arr=[0]*n
        arr[0]=suff[1]
        for i in range(1,n-1):
            arr[i]=suff[i+1]*pref
            pref*=nums[i]
        arr[n-1]=pref
        return arr


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends