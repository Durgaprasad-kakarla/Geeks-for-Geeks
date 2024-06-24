#User function Template for python3

class Solution:
    def sumMatrix(self, n, q):
        # code here 
        first_row=2+n-1
        if q<first_row:
            return q-2+1
        if first_row+(n-1)<q:
            return 0
        tot_rows=n-(q-n-1)
        return tot_rows


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n, q = map(int, input().split())

        ob = Solution()
        print(ob.sumMatrix(n, q))

# } Driver Code Ends