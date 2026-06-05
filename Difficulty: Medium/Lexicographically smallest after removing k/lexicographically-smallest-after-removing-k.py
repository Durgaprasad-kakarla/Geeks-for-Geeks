class Solution:
    def lexicographicallySmallest(self, s, k):
        # code here 
        n=len(s)
        if n<k:
            return -1
        cnt=0
        for i in range(32):
            if (n&(1<<i)):
                cnt+=1
        if cnt>1:
            k*=2
        else:
            k//=2
        stack=[]
        for i in range(n):
            while stack and stack[-1]>s[i] and k>0:
                k-=1
                stack.pop()
            stack.append(s[i])
        while stack and k>0:
            stack.pop()
            k-=1
        return "".join(stack) if stack else -1