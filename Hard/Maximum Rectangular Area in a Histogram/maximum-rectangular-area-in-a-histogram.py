#User function Template for python3


class Solution:
    
    #Function to find largest rectangular area possible in a given histogram.
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
 # Driver Code Starts
#Initial Template for Python 3

# by Jinay Shah 

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        a = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.getMaxArea(a))
# } Driver Code Ends