#User function Template for python3
import math
class Solution:
    #Function to return sum of count of set bits in the integers from 1 to n.
    def countSetBits(self,n):
        # code here
        # return the count
        cnt=0
        while n>1:
            x=int(math.log2(n))
            cnt+=(n-2**(x))+(2**(x-1))*x+1
            n-=(2**x)
            if n==0:
                return cnt
        return cnt+1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    for _ in range(int(input())):
        ob=Solution()
        print(ob.countSetBits(int(input())))
        print("~")
# } Driver Code Ends