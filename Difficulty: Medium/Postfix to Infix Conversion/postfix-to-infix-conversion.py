#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def postToInfix(self, postfix):
        # Code here
        n=len(postfix)
        op=("*","/",'+','-')
        stack=[]
        for i in range(n):
            if postfix[i] in op:
                peak1=stack.pop()
                peak2=stack.pop()
                stack.append('('+peak2+postfix[i]+peak1+')')
            else:
                stack.append(postfix[i])
        return stack[-1]

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        postfix = input()
        ob = Solution()
        res = ob.postToInfix(postfix)
        print(res)
        print("~")
# } Driver Code Ends