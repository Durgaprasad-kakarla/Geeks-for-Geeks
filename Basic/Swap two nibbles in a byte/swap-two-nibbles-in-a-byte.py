#User function Template for python3
class Solution:
    def swapNibbles (self, n):
        # code here 
        s=""
        for i in range(7,-1,-1):
            if n&(1<<i):
                s+='1'
            else:
                s+='0'
        return int(s[4:]+s[:4],2)


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())

        ob = Solution()
        print(ob.swapNibbles(n))

# } Driver Code Ends