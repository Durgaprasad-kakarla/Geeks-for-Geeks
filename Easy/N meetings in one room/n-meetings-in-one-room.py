#User function Template for python3

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,N,S,F):
        # code here
        arr=[]
        for i in range(N):
            arr.append([S[i],F[i]])
        dic={}
        for i in range(N):
            if (arr[i][0],arr[i][1]) not in dic:
                dic[(arr[i][0],arr[i][1])]=i+1
        arr=sorted(arr,key=lambda x:x[1])
        cnt=0
        ele=-1
        for i in range(N):
            if arr[i][0]>ele:
                cnt+=1
                ele=arr[i][1]
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
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends