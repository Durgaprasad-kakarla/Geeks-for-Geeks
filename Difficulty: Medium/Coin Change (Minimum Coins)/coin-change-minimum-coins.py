class Solution:
	def minCoins(self, coins, amount):
		# code here
        curr=[float('inf') for i in range(amount+1)]
        curr[0]=0
        coins.sort()
        n=len(coins)
        for i in range(1,n+1):
            if coins[i-1]>amount:
                break
            for j in range(coins[i-1],amount+1):
                l=1+curr[j-coins[i-1]]
                r=curr[j]
                curr[j]=min(l,r)
        return curr[amount] if curr[amount]!=float('inf') else -1
                
#{ 
 # Driver Code Starts
#Initial Template for Python 3
#Position this line where user code will be pasted.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        k = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.minCoins(arr, k)
        print(res)
        print("~")
        t -= 1

# } Driver Code Ends