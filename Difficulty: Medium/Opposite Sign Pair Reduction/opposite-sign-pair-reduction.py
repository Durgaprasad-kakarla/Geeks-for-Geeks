class Solution:
    def reducePairs(self, arr):
        # code here
        n=len(arr)
        stack=[]
        for i in range(n):
            skip_curr=False
            while stack and ((stack[-1]>0 and arr[i]<0) or (stack[-1]<0 and arr[i]>0)):
                ele=stack[-1]
                if abs(ele)>abs(arr[i]):
                    skip_curr=True
                    break
                elif abs(ele)==abs(arr[i]):
                    stack.pop()
                    skip_curr=True
                    break
                else:
                    stack.pop()
            if not skip_curr:
                stack.append(arr[i])
            # print(stack)
        return stack
                