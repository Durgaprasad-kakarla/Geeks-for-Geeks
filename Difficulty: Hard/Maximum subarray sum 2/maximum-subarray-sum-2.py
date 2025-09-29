from collections import deque
class Solution:
    def maxSubarrSum(self, arr, a, b):
        # code here
        n=len(arr)
        queue=deque()
        pref=[0]*(n+1)
        for i in range(1,n+1):
            pref[i]=pref[i-1]+arr[i-1]
        maxi=-float('inf')
        for i in range(1,b):
            while queue and queue[0][0]<=pref[i]:
                queue.popleft()
            queue.appendleft([pref[i],i])
        for i in range(n-a+1):
            while i+b<=n and queue and queue[0][0]<=pref[i+b]:
                queue.popleft()
            if i+b<=n:
                queue.appendleft([pref[i+b],i+b])
            while queue and queue[-1][1]<i+a:
                queue.pop()
            maxi=max(maxi,queue[-1][0]-pref[i])
        return maxi
 

        