#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def postToPre(self, post_exp):
        # Code here
        def postToInfix(s):
            n=len(s)
            op=('/','*','+','-')
            stack=[]
            for i in range(n):
                if s[i] in op:
                    peak1=stack.pop()
                    peak2=stack.pop()
                    stack.append('('+peak2+s[i]+peak1+')')
                else:
                    stack.append(s[i])
            return stack[-1]
        def infToPostfix(s):
            n=len(s)
            precedence={'*':2,'/':2,'+':1,'-':1}
            stack=[]
            postfix=''
            for i in range(n-1,-1,-1):
                if s[i] in precedence:
                    while stack and stack[-1]!=')' and precedence[s[i]]<=precedence[stack[-1]]:
                        postfix+=stack.pop()
                    stack.append(s[i])
                elif s[i]==')':
                    stack.append(s[i])
                elif s[i]=='(':
                    while stack:
                        if stack[-1]==')':
                            stack.pop()
                            break
                        postfix+=stack.pop()
                else:
                    postfix+=s[i]
            return postfix
        s=postToInfix(post_exp)
        return infToPostfix(s)[::-1]

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        postfix = input()
        ob = Solution()
        res = ob.postToPre(postfix)
        print(res)
        print("~")
# } Driver Code Ends