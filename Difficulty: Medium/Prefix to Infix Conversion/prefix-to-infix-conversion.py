#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def preToInfix(self, s):
        # Code here
        stack=[]
        n=len(s)
        op=('+','-','*','/','%','^')
        for i in range(n-1,-1,-1):
            if s[i] in op:
                peak1=stack.pop()
                peak2=stack.pop()
                stack.append('('+peak1+s[i]+peak2+')')
            else:
                stack.append(s[i])
        return stack[-1]

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        prefix = input()
        ob = Solution()
        res = ob.preToInfix(prefix)
        print(res)
        print("~")
# } Driver Code Ends