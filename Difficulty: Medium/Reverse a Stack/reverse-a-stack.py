#User function Template for python3

from typing import List

class Solution:
    def reverse(self,St): 
        #code here
        def reverse_stack(St):
            if St:
                queue.append(St.pop())
                reverse_stack(St)
        queue=[]
        reverse_stack(St)
        while queue:
            St.append(queue.pop(0))
        
#{ 
 # Driver Code Starts

#Initial Template for Python 3

 
for _ in range(int(input())):
    N = int(input())
    St = list(map(int, input().split()))
    ob = Solution()
    ob.reverse(St)
    print(*St)
    print("~")
# } Driver Code Ends