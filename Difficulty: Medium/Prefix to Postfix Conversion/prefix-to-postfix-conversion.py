#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def preToPost(self, pre_exp):
        # Code here
        def preToInfix(s):
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
        def infToPostfix(s):
            n=len(s)
            stack=[]
            precedence={'^':3,'*':2,'/':2,'+':1,'-':1}
            postfix=""
            for i in range(n):
                if s[i] in precedence:
                    while stack and stack[-1]!='(' and precedence[s[i]]<=precedence[stack[-1]]:
                        postfix+=stack.pop()
                    stack.append(s[i])
                elif s[i]=='(':
                    stack.append(s[i])
                elif s[i]==')':
                    while stack:
                        if stack[-1]=='(':
                            stack.pop()
                            break
                        postfix+=stack.pop()
                else:
                    postfix+=s[i]
            while stack:
                postfix+=stack.pop()
            return postfix
        s=preToInfix(pre_exp)
        return infToPostfix(s)

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        prefix = input()
        ob = Solution()
        res = ob.preToPost(prefix)
        print(res)
        print("~")
# } Driver Code Ends