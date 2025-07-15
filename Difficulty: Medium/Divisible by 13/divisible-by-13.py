class Solution:
    def divby13(self, s):
        # code here 
        carry=0
        n=len(s)
        for i in range(0,n,2):
            carry=(int(str(carry)+(s[i:i+2]).strip(" ")))%13
        if carry==0:
            return True
        return False