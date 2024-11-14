#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        max1,max2=-float('inf'),-float('inf')
        n=len(arr)
        for i in range(n):
            if max1<arr[i]:
                max2=max1
                max1=arr[i]
            elif arr[i]!=max1 and max2<arr[i]:
                max2=arr[i]
        return -1 if max2==-float('inf') else max2


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.getSecondLargest(arr)
        print(ans)
        print("~")
# } Driver Code Ends