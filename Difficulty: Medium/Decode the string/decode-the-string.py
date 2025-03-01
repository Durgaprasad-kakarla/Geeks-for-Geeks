
class Solution:
    def decodedString(self, s):
        # code here
        stack=[]
        i=len(s)-1
        while i>=0:
            if s[i]=='[':
                num=''
                i-=1
                while i>=0 and s[i].isnumeric():
                    num+=s[i]
                    i-=1
                num=num[::-1]
                st=''
                while stack and stack[-1]!=']':
                    st+=stack.pop()
                stack.pop()
                stack.append(int(num)*st)
            else:
                stack.append(s[i])
                i-=1
        return "".join(stack[::-1])
                
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()

        ob = Solution()
        print(ob.decodedString(s))
        print("~")

# } Driver Code Ends