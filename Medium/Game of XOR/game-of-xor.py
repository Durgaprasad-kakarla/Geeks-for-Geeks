#User function Template for python3

class Solution:
    def gameOfXor(self, N , A):
        # code here 
        if N&1==0:
            return 0
        xor=0
        for i in range(N):
            if i%2==0:
                xor=xor^A[i]
        return xor


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N=int(input())
        A=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.gameOfXor(N,A))
# } Driver Code Ends