#User function Template for python3

class Solution:
    def cutRod(self, price):
        #code here
        n=len(price)
        def cutting_rod(ind,W):
            if ind==0:
                return W*price[ind]
            if dp[ind][W]!=-1:
                return dp[ind][W]
            l=-float('inf')
            if W>=(ind+1):
                l=price[ind]+cutting_rod(ind,W-(ind+1))
            r=cutting_rod(ind-1,W)
            dp[ind][W]=max(l,r)
            return max(l,r)
        dp=[[-1 for _ in range(n+1)] for _ in range(n)]
        return cutting_rod(n-1,n)
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        # n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.cutRod(a))

        T -= 1

        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends