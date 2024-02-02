#User function template for Python

class Solution:
    # your task is to complete this function
    # function should return an integer
    def atoi(self,s):
        # Code here
        new_st=""
        s=''
        i=0
        while i<len(string):
            if string[i]!=' ':
                s=string[i:]
                break
            i+=1
        if s=='':
            return -1
        sign=''
        if s[0]=='+' or s[0]=='-':
            sign=s[0]
        if sign!='':
            x=1
        else:
            x=0
        for i in range(x,len(s)):
            if s[i].isdigit():
                new_st+=s[i]
            else:
                return -1
        if new_st=='':
            return -1
        if sign=='-':
            if -int(new_st)<-2**31:
                return -2**31
            return -int(new_st)
        else:
            if int(new_st)>(2**31-1):
                return 2**31-1
            return int(new_st) 


#{ 
 # Driver Code Starts
#Initial template for Python

if __name__=='__main__':
    t=int(input())
    for i in range(t):
        string = input().strip();
        ob=Solution()
        print(ob.atoi(string))
# } Driver Code Ends