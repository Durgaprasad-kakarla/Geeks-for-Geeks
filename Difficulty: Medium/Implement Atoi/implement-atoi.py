class Solution:
    def myAtoi(self, s):
        # code here
        s=s.strip(' ')
        sign=''
        if s[0]=='+' or s[0]=='-':
            sign=s[0]
            s=s[1:]
        # print(sign)
        s=s.lstrip('0')
        n=len(s)
        ans=''
        for i in range(n):
            if s[i].isdigit():
                ans+=s[i]
            else:
                break
        if ans=='':
            return 0
        # print(ans)
        if sign!='':
            if sign=='+':
                if int(ans)>2147483647:
                    return 2147483647
                return ans
            else:
                # print(sign,ans)
                if -1*int(ans)<-2147483648:
                    return -2147483648
                return sign+ans
        else:
            if int(ans)>2147483647:
                    return 2147483647
            return ans
        