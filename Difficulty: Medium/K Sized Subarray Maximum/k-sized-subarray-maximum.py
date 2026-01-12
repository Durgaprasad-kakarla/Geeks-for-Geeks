class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        n=len(arr)
        queue=deque()
        window_max=[]
        for i in range(n):
            while queue and queue[0][1]<=(i-k):
                queue.popleft()
            while queue and queue[-1][0]<arr[i]:
                queue.pop()
            queue.append([arr[i],i])
            if i>=k-1:
                window_max.append(queue[0][0])
        return window_max
            