#User function Template for python3


class Solution:
    
    #Function to convert an infix expression to a postfix expression.
    def InfixtoPostfix(self, s):
        #code here
        precedence={'^':3,'*':2,'/':2,'+':1,'-':1}
        stack,postfix=[],""
        n=len(s)
        for i in range(n):
            while stack and stack[-1]!='(' and s[i] in precedence and precedence[s[i]]<=precedence[stack[-1]]:
                postfix+=stack.pop()
            while stack and s[i]==')':
                if stack[-1]=='(':
                    stack.pop()
                    break
                postfix+=stack.pop()
            if s[i] in precedence or s[i]=='(':
                stack.append(s[i])
            elif s[i]==')':
                continue
            else:
                postfix+=s[i]
        while stack:
            postfix+=stack.pop()
        return postfix


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# This code is contributed by Nikhil Kumar Singh(nickzuck_007)

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        exp = str(input())
        ob = Solution()
        print(ob.InfixtoPostfix(exp))
        print("~")

# } Driver Code Ends