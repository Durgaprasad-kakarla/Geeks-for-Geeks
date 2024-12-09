#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def minRemoval(self, intervals):
        # Code here
        intervals.sort(key=lambda x:x[1])
        start,end=intervals[0][0],intervals[0][1]
        n=len(intervals)
        # print(intervals)
        cnt=0
        for i in range(1,n):
            s,e=intervals[i]
            if end<=e and end>s:
                cnt+=1
            else:
                start,end=s,e
        return cnt

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        ob = Solution()
        res = ob.minRemoval(intervals)
        print(res)
        print("~")
# } Driver Code Ends