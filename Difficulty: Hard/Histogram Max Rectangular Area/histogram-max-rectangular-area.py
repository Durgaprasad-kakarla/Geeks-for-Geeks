#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends


class Solution:
    def getMaxArea(self,nums):
        #code here
        stack=[]
        n=len(nums)
        maxi=0
        for i in range(n):
            ind=i
            while stack and stack[-1][1]>nums[i]:
                maxi=max(maxi,(i-stack[-1][0])*stack[-1][1])
                ind=stack[-1][0]
                stack.pop()
            stack.append([ind,nums[i]])
        while stack:
            ind,ele=stack.pop()
            maxi=max(maxi,(n-ind)*ele)
        return maxi


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.getMaxArea(arr)
        print(res)
        print("~")
        t -= 1


# } Driver Code Ends