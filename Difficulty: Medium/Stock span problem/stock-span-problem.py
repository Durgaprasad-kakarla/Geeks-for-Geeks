#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def calculateSpan(self, arr):
        #write code here
        stack=[]
        n=len(arr)
        stocks=[1]*n
        for i in range(n):
            cnt=0
            while stack and stack[-1][0]<=arr[i]:
                cnt+=stack[-1][1]
                stack.pop()
            stocks[i]+=cnt
            stack.append([arr[i],stocks[i]])
        return stocks

#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.calculateSpan(arr)
        print(*ans)
        print("~")
        t -= 1
# } Driver Code Ends