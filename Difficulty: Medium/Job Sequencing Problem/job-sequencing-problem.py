class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        n=len(deadline)
        heap,arr=[],[]
        for i in range(n):
            arr.append([deadline[i],profit[i]])
        arr.sort()
        for job in arr:
            heapq.heappush(heap,job[1])
            while len(heap)>job[0]:
                heapq.heappop(heap)
        return len(heap),sum(heap)
#{ 
 # Driver Code Starts
#Initial Template for Python 3
import heapq

#Position this line where user code will be pasted.

if __name__ == "__main__":
    t = int(input().strip())

    for _ in range(t):
        deadline = list(map(int, input().strip().split()))
        profit = list(map(int, input().strip().split()))

        obj = Solution()
        ans = obj.jobSequencing(deadline, profit)
        print(ans[0], ans[1])
        print("~")
# } Driver Code Ends