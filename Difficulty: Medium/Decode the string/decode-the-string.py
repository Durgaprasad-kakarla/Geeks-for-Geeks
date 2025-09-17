class Solution:
    def decodedString(self, s):
        # code here
        n=len(s)
        stack=[]
        i=n-1
        while i>=0:
            if stack and s[i].isdigit():
                num=s[i]
                i-=1
                while i>=0 and s[i].isdigit():
                    num+=s[i]
                    i-=1
                stack.pop()
                st=''
                while stack and stack[-1]!=']':
                    st+=stack.pop()
                stack.pop()
                stack.append(st*int(num[::-1]))
            else:
                stack.append(s[i])
                i-=1
        return "".join(stack[::-1])