from collections import deque
class Solution:
    def generateIp(self, s):
        # Code here
        n=len(s)
        queue=deque([['','',0,0]])
        ans=[]
        try:
            while queue:
                curr,st,k,ind=queue.popleft()
                if k==3 and ind==n:
                    ans.append(st)
                    continue
                if k>4 or ind>=n :
                    continue
                if int(curr+s[ind])<256:
                    queue.append([curr+s[ind],st+s[ind],k,ind+1])
                    if curr:
                        queue.append([s[ind],st+'.'+s[ind],k+1,ind+1])
                else:
                    queue.append([s[ind],st+'.'+s[ind],k+1,ind+1])
                # print(queue)
            ip_address=[]
            for i in range(len(ans)):
                s=ans[i]
                s=s.split('.')
                flag=0
                for j in s:
                    if len(j)>0 and j[0]=='0' and len(j)>1:
                        flag=1
                        break
                if flag==0:
                    ip_address.append(".".join(s))
            return ip_address
        except Exception as e:
            print(e)
            print(ind,len(s))
            return []