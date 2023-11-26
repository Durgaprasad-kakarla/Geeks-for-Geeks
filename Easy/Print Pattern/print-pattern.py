#User function Template for python3

class Solution:
    def pattern(self, n):
        # code here
        lst=[]
        while n>0:
            lst.append(n)
            n-=5
        lst=lst+[n]+lst[::-1]
        return lst

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end = " ")
        print()
# } Driver Code Ends