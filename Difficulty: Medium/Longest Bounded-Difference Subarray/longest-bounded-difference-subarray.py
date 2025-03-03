from collections import deque
class Solution:
    def longestSubarray(self, arr, x):
        n = len(arr)
        left = right = 0
        max_len = 0
        start = 0
    
        min_deque = deque()
        max_deque = deque() 
    
        while right < n:
            while min_deque and arr[min_deque[-1]] > arr[right]:
                min_deque.pop()
            min_deque.append(right)
    
            while max_deque and arr[max_deque[-1]] < arr[right]:
                max_deque.pop()
            max_deque.append(right)
            
            while arr[max_deque[0]] - arr[min_deque[0]] > x:
                if min_deque[0] == left:
                    min_deque.popleft()
                if max_deque[0] == left:
                    max_deque.popleft()
                left += 1
                
            if right - left + 1 > max_len:
                max_len = right - left + 1
                start = left
    
            right += 1
    
        return arr[start:start + max_len]

#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        k = int(input().strip())
        ob = Solution()
        ans = ob.longestSubarray(arr, k)

        print(" ".join(map(str, ans)))
        tc -= 1
        print("~")

# } Driver Code Ends