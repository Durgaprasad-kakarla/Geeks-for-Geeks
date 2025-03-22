class Solution:
    def maxValue(self, arr):
        # code here
        def max_amount(arr):
            n=len(arr)
            dp=[0]*(n+1)
            dp[1]=arr[0]
            for i in range(2,n+1):
                l=dp[i-1]
                r=-float("inf")
                if i>1:
                    r=dp[i-2]+arr[i-1]
                dp[i]=max(l,r)
            return dp[-1]
        return max(max_amount(arr[1:]),max_amount(arr[:-1]))


#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self):
        arr = [int(i) for i in input().strip().split()]
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = IntArray().Input()

        obj = Solution()
        res = obj.maxValue(arr)

        print(res)
        print("~")

# } Driver Code Ends