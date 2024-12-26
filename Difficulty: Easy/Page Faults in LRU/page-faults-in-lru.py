#User function Template for python3
from collections import deque
class Solution:
    def pageFaults(self, n, C, pages):
        # code here
        queue=deque()
        cnt=0
        for i in range(n):
            found=False
            for j in range(len(queue)):
                if queue[j]==pages[i]:
                    found=True
                    break
            if not found:
                if len(queue)<C:
                    queue.append(pages[i])
                else:
                    queue.popleft()
                    queue.append(pages[i])
                cnt+=1
            else:
                queue.remove(pages[i])
                queue.append(pages[i])
        return cnt
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
        pages = input().split()
        for itr in range(N):
            pages[itr] = int(pages[itr])
        C = int(input())

        ob = Solution()
        print(ob.pageFaults(N, C, pages))

# } Driver Code Ends