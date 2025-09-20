class Solution:
    def longestSubarray(self, arr):
        n = len(arr)
        left, right = [-1]*n, [n]*n
        
        # for each position, we will find the left bigger's and right bigger's index
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] < arr[i]:
                right[stack.pop()] = i
            stack.append(i)
        
        stack.clear()
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] < arr[i]:
                left[stack.pop()] = i
            stack.append(i)

        ans = 0
        for i in range(n):
            length = right[i]-left[i]-1
            if length >= arr[i]:
                ans = max(ans, length)
        return ans