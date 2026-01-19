class Solution:
    def removeKdig(self, s, k):
        # code here
        n=len(s)
        stack=[]
        for i in range(n):
            while stack and k>0 and stack[-1]>s[i]:
                stack.pop()
                k-=1
            stack.append(s[i])
        while stack and k>0:
            stack.pop()
            k-=1
        s="".join(stack).lstrip('0')
        return '0' if s=='' else s
        