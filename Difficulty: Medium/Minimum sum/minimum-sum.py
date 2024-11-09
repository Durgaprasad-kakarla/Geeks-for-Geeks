#User function Template for python3
from collections import Counter
class Solution:
    def minSum(self, arr):
        # code here
        arr.sort(reverse=True)
        n = len(arr)
        while arr[n - 1] == 0:
            n -= 1
        output = []
        carry = 0
        for i in range(1, n, 2):
            carry, r = divmod(arr[i - 1] + arr[i] + carry, 10)
            output.append(str(r))
        if n & 1:  # if odd
            carry += arr[n - 1]
        if carry:
            output.append(str(carry))
        return "".join(reversed(output))

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.minSum(arr)
        print(ans)
        tc -= 1

        print("~")

# } Driver Code Ends