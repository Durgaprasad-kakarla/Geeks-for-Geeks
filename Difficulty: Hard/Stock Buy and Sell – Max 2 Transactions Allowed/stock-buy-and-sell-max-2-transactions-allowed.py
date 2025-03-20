class Solution:
    def maxProfit(self, prices):
        # code here
        prev=[[0 for i in range(3)]for j in range(2)]
        for ind in range(len(prices)-1,-1,-1):
            cur=[[0 for i in range(3)]for j in range(2)]
            for buy in range(2):
                for limit in range(1,3):
                    if buy:
                        cur[buy][limit] = max(-prices[ind] + prev[0][limit],prev[1][limit])
                    else:
                        cur[buy][limit] = max(prices[ind] + prev[1][limit-1],prev[0][limit])
            prev=cur
        return prev[1][2]

#{ 
 # Driver Code Starts
#Initial template for Python 3
import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxProfit(arr))
        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends