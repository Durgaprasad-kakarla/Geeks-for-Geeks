
class Solution:
    def maxLength(self, s):
        # code here
        stack=[]
        n=len(s)
        maxi=0
        for i in range(n):
            if stack and s[i]==')' and stack[-1][1]=='(':
                stack.pop()
                if stack:
                    maxi=max(maxi,i-stack[-1][0])
                else:
                    maxi=max(maxi,i+1)
            else:
                stack.append([i,s[i]])
        return maxi

#{ 
 # Driver Code Starts
# Initial Template for Python3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S = input()

        ob = Solution()
        print(ob.maxLength(S))
        print("~")

# } Driver Code Ends