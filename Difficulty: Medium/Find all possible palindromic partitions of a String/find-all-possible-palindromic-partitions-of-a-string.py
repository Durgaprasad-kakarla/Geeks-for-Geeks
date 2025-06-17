class Solution:
    def palinParts (self, s):
        # code here
        def partitions(ind,temp,s,n):
            if ind==n:
                ans.append(temp.copy())
                return 
            for i in range(ind+1,n+1):
                if s[ind:i]==s[ind:i][::-1]:
                    partitions(i,temp+[s[ind:i]],s,n)
        ans=[]
        partitions(0,[],s,len(s))
        return ans

