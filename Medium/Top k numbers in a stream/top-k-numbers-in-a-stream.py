#User function Template for python3

class Solution:
    def kTop(self,arr,n,k):
        #code here.
        res=[]
        top=[0 for i in range(k+1)]
        dic={i:0 for i in range(k+1)}
        
        for i in range(n):
            if arr[i] in dic:
                dic[arr[i]]+=1
            else:
                dic[arr[i]]=1
            top[k]=arr[i]
            i=top.index(arr[i])
            i-=1
            while i>=0:
                if dic[top[i]]==dic[top[i+1]] and (top[i]>top[i+1]):
                    top[i],top[i+1]=top[i+1],top[i]
                elif dic[top[i]]<dic[top[i+1]]:
                    top[i],top[i+1]=top[i+1],top[i]
                else:
                    break
                i-=1
            i=0
            ans=[]
            while i<k and top[i]!=0:
                ans.append(top[i])
                i+=1
            res.append(ans)
        return res
                
        


#{ 
 # Driver Code Starts


t=int(input())
for _ in range(0,t):
    n,k=list(map(int,input().split()))
    a=list(map(int,input().split()))
    ob = Solution()
    ans=ob.kTop(a,n,k)
    for line in ans:
        print(*line)



# } Driver Code Ends