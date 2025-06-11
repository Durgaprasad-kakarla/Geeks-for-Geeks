#User function Template for python3
class Solution:
    def findLength(self, color, radius):
        n=len(color)
        stack=[]
        for i in range(n):
            if stack and stack[-1]==[color[i],radius[i]]:
                stack.pop()
            else:
                stack.append([color[i],radius[i]])
        return len(stack)
            
        