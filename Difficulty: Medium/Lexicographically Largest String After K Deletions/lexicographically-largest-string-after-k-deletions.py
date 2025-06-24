class Solution:
    def maxSubseq(self, s, k):
        #code here
        stack=[]
        n=len(s)
        for i in range(n):
            while stack and stack[-1]<s[i] and k>0:
                stack.pop()
                k-=1
            stack.append(s[i])
        while stack and k>0:
            stack.pop()
            k-=1
        return "".join(stack)
        
