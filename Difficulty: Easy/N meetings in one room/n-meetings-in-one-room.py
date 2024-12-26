#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,start,end):
        # code here
        arr=[]
        n=len(start)
        for i in range(n):
            arr.append([start[i],end[i]])
        arr.sort(key=lambda x:x[1])
        end,cnt=arr[0][1],1
        for i in range(1,n):
            if arr[i][0]>end:
                end=arr[i][1]
                cnt+=1
        return cnt


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        start = list(map(int, input().strip().split()))
        end = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.maximumMeetings(start, end))
        print("~")

# } Driver Code Ends