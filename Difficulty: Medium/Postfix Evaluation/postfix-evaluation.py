class Solution:
    def evaluatePostfix(self, arr):
        # code here
        n=len(arr)
        stack=[]
        for i in range(n):
            if arr[i]=='*' or arr[i]=='+' or arr[i]=='-' or arr[i]=='/' or arr[i]=='^':
                if len(stack)>1:
                    num1=int(stack.pop())
                    num2=int(stack.pop())
                    if arr[i]=='/':
                        stack.append(num2//num1)
                    elif arr[i]=='*':
                        stack.append(num2*num1)
                    elif arr[i]=='+':
                        stack.append(num2+num1)
                    elif arr[i]=='-':
                        stack.append(num2-num1)
                    else:
                        stack.append(num2**num1)
            else:
                stack.append(arr[i])
        return (stack[-1])
        