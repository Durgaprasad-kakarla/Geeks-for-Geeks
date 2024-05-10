#User function Template for python3
import math
class Solution:
    def jugglerSequence(self, n):
        # code here
        jogg_seq=[n]
        while jogg_seq[-1]!=1:
            if jogg_seq[-1]&1==1:
                jogg_seq.append(math.floor(jogg_seq[-1]**(3/2)))
            else:
                jogg_seq.append(math.floor(jogg_seq[-1]**(1/2)))
        return jogg_seq

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        arr = ob.jugglerSequence(n)
        for i in (arr):
            print(i, end=" ")
        print()

# } Driver Code Ends