class Solution:
    def smallestWindow(self, s, p):
        # code here
        n,m=len(s),len(p)
        dic={}
        for i in range(m):
            if p[i] in dic:
                dic[p[i]]+=1
            else:
                dic[p[i]]=1
        start=0
        mini=float('inf')
        ind=-1
        for i in range(n):
            if s[i] in dic:
                dic[s[i]]-=1
            flag=0
            for j in dic:
                if dic[j]>0:
                    flag=1
                    break
            if flag==0:
                while start<n:
                    if mini>(i-start+1):
                        mini=i-start+1
                        ind=start
                    if s[start] in dic:
                        dic[s[start]]+=1
                        if dic[s[start]]>0:
                            start+=1
                            break
                    start+=1
        if ind==-1:
            return ""
        return s[ind:ind+mini]