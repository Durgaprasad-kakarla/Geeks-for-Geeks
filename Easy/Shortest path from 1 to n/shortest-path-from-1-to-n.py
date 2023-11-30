#User function Template for python3

class Solution:
    def minimumStep (self, n):
        #complete the function here
        cnt=0
        while n!=1:
            if n%3==0:
                n=n//3
            else:
                n-=1
            cnt+=1
        return cnt
        return cnt+n#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = int(input())
        ob = Solution()
        print(ob.minimumStep(n))
# } Driver Code Ends