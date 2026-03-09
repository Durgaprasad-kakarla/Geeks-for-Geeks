class Solution:
    def largestSwap(self, s):
        #code here
        n=len(s)
        dic={}
        for i in range(n):
            dic[s[i]]=i
        flag,lst=0,list(s)
        for i in range(n):
            curr=int(s[i])
            for j in range(10,curr,-1):
                if str(j) in dic and int(s[i])<j and i<dic[str(j)]:
                    flag=1
                    ind,i=dic[str(j)],i
                    lst[i],lst[ind]=lst[ind],lst[i]
                    break
            if flag==1:
                break
        return "".join(lst)