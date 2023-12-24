#User function Template for python3

class Solution:
    def nextPermutation(self, N, nums):
        # code here
        ind=-1
        n=len(nums)
        for i in range(n-1,0,-1):
            if nums[i]>nums[i-1]:
                ind=i-1
                break
        if ind==-1:
            return nums[::-1]
        greater=-1
        for i in range(n-1,ind,-1):
            if nums[ind]<nums[i]:
                greater=i
                break
        nums[ind],nums[greater]=nums[greater],nums[ind]
        return nums[:ind+1]+nums[ind+1:][::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        arr = input().split()
        for i in range(N):
            arr[i] = int(arr[i])
        
        ob = Solution()
        ans = ob.nextPermutation(N, arr)
        for i in range(N):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends