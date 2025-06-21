from collections import deque
class Solution:
    def catchThieves(self, arr, k):
        #code  here
        stack=[]
        n=len(arr)
        cnt=0
        queue,stack=deque(),[]
        for i in range(n-1,-1,-1):
            if arr[i]=='T':
                stack.append(i)
        for i in range(n):
            if arr[i]=='P':
                flag=0
                while queue and (i-queue[0]>k or (i-queue[0]<=k and arr[queue[0]]==-1)):
                    queue.popleft()
                if queue and i-queue[0]<=k:
                    arr[queue[0]]=-1
                    cnt+=1
                    flag=1
                    queue.popleft()
                if flag==0:
                    while stack and stack[-1]<=i:
                        stack.pop()
                    if stack and stack[-1]-i<=k:
                        arr[stack[-1]]=-1
                        cnt+=1
                        stack.pop()
            else:
                queue.append(i)
        return cnt
            
                    
                
                    