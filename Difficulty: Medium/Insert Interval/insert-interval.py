#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        intervals.sort()
        n=len(intervals)
        ans=[]
        start,end,flag=-1,-1,1
        for i in range(n):
            s,e=intervals[i]
            if (newInterval[0]>=s and newInterval[0]<=e) or (newInterval[1]>=s and newInterval[1]<=e) or (newInterval[1]>=e and newInterval[0]<=s):
                start=min(s,newInterval[0])
                end=max(e,newInterval[1])
                newInterval[0],newInterval[1]=start,end
                flag=0
            else:
                if start==-1 and end==-1:
                    if newInterval[0]<s and newInterval[1]<s and flag:
                        ans.append(newInterval)
                        ans.append([s,e])
                        flag=0
                    else:
                        ans.append([s,e])
                else:
                    ans.append([start,end])
                    ans.append([s,e])
                    start,end=-1,-1
        if flag==1:
            ans.append(newInterval)
        if start==-1 and end==-1:
            return ans
        ans.append([start,end])
        return ans
                    

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        N = int(input())
        intervals = [list(map(int, input().split())) for i in range(N)]
        newEvent = list(map(int, input().split()))
        ob = Solution()
        res = ob.insertInterval(intervals, newEvent)
        print('[', end = '')
        for i in range(len(res)):
            print('[', end = '')
            print(str(res[i][0])+','+str(res[i][1]), end = '')
            print(']', end = '')
            if i < len(res)-1:
                print(',', end='')
        print(']')
        print("~")
# } Driver Code Ends