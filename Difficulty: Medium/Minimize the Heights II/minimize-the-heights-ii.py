#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        n=len(arr)
        arr.sort()
        ans=arr[n-1]-arr[0]
        mini=arr[0]+k
        maxi=arr[n-1]-k
        for i in range(n-1):
            cur_mini=min(mini,arr[i+1]-k)
            cur_maxi=max(maxi,arr[i]+k)
            if cur_mini>=0:
                ans=min(ans,cur_maxi-cur_mini)
        return ans
            
        #User function Template for python3

# class Solution:
#     def getMinDiff(self, nums, n, k):
#         # code here
#         nums.sort()
#         ans=nums[n-1]-nums[0]
#         mini=nums[0]+k
#         maxi=nums[n-1]-k
#         for i in range(n-1):
#             cur_mini=min(nums[i+1]-k,mini)
#             cur_maxi=max(nums[i]+k,maxi)
#             if cur_mini>=0:
#                 ans=min(ans,cur_maxi-cur_mini)
#         return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        # n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, k)
        print(ans)
        tc -= 1

# } Driver Code Ends