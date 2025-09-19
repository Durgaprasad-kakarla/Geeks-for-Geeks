class Solution:
    def minParentheses(self, s):
        # code here
        n=len(s)
        stack=[]
        for i in range(n):
            if stack and stack[-1]=='(' and s[i]==')':
                stack.pop()
            else:
                stack.append(s[i])
        return len(stack)