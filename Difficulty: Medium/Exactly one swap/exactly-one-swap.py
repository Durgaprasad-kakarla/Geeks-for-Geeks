class Solution:
    def countStrings(self, s): 
        #code here
        n=len(s)
        dic,cnt,flag={},0,0
        for i in range(n-1,-1,-1):
            if s[i] in dic:
                cnt+=(n-i-1-dic[s[i]])
            else:
                cnt+=(n-i-1)
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
            if dic[s[i]]>1:
                flag=1
        return cnt+flag
        