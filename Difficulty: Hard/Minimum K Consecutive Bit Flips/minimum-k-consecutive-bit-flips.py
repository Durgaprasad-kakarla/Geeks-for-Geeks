from collections import deque
class Solution:
    def kBitFlips(self, nums, k):
        # code here
        queue=deque()
        tot_operations=0
        n=len(arr)
        for i in range(n):
            while queue and i>queue[0]+k-1:
                queue.popleft()
            if (nums[i]+len(queue))%2==0:
                if i+k>n:
                    return -1
                tot_operations+=1
                queue.append(i)
        return tot_operations