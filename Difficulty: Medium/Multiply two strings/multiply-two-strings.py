#User function Template for python3

class Solution:
    def multiplyStrings(self, s1, s2):
        # code here
        # return the product string
        op1,op2="",""
        if not s1[0].isnumeric():
            op1=s1[0]
            s1=s1[1:]
        if not s2[0].isnumeric():
            op2=s2[0]
            s2=s2[1:]
        s1=int(s1)
        s2=int(s2)
        if op1=='-' and op2=='-':
            return s1*s2
        elif op1=='-' or op2=='-':
            return -(s1*s2)
        return s1*s2


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        a = input()
        b = input()
        print(Solution().multiplyStrings(a.strip(), b.strip()))

        print("~")

# } Driver Code Ends