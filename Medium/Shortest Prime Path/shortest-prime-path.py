#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
from collections import deque
class Solution:
    def solve (self,num1,num2):
        #code here
        max_num=9999
        prime=[1]*(10001)
        prime[1]=0
        i=2
        for i in range(2, int(max_num**0.5) + 1):
            if prime[i]:
                for j in range(i*i, max_num + 1, i):
                    prime[j] = 0
        dp=[-1]*(10001)
        vis=[0]*(10001)
        queue=deque()
        queue.append(num1)
        dp[num1]=0
        vis[num1]=0
        while queue:
            curr=queue.popleft()
            if vis[curr]:
                continue
            vis[curr]+=1
            s=str(curr)
            for i in range(4):
                for ch in range(10):
                    ch=str(ch)
                    if ch==s[i] or (ch=='0' and i==0):
                        continue
                    nxt=list(s)
                    nxt[i]=ch
                    next_num=int("".join(nxt))
                    if prime[next_num] and dp[next_num]==-1:
                        dp[next_num]=1+dp[curr]
                        queue.append(next_num)
                    if next_num==num2:
                        return dp[next_num]
        return dp[num2]


#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        Num1,Num2=map(int,input().split())
        ob = Solution()
        print(ob.solve(Num1,Num2))
# } Driver Code Ends