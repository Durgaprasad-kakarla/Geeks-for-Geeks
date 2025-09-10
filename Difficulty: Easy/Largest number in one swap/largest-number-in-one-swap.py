class Solution:
    def largestSwap(self, s):
        #code here 3044 4043
        maxi,max_ind,zero_ind='',-1,-1
        n=len(s)
        for i in range(n-1,-1,-1):
            if maxi<s[i]:
                maxi=s[i]
                max_ind=i
        lst=list(s)
        for i in range(n):
            if s[i]<maxi and max_ind>0:
                lst[i],lst[max_ind]=lst[max_ind],lst[i]
                break
        return "".join(lst)