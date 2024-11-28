#User function template for Python
class Solution:
    def myAtoi(self, s):
        # Code here
        n=len(s)
        i=0
        while i<n:
            if s[i]==' ' or s[i]=='0':
                i+=1
            else:
                break
        sign=''
        if i<n and (s[i]=='-' or s[i]=='+'):
            sign=s[i]
            i+=1
        if i<n and s[i].isdigit():
            start=i
            while i<n and s[i].isdigit():
                i+=1
            if sign=='' or sign=='+':
                if int(s[start:i])>(2**31-1):
                    return 2**31-1
                else:
                    return int(s[start:i])
            else:
                if -1*int(s[start:i])<(-2**31):
                    return -2**31
                else:
                    return -1*int(s[start:i])
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = input()
        ob = Solution()
        print(ob.myAtoi(s))
        print("~")

# } Driver Code Ends