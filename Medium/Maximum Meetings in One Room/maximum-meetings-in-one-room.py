from typing import List


class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        # code here
        arr=[]
        for i in range(N):
            arr.append([S[i],F[i]])
        dic={}
        for i in range(N):
            if (arr[i][0],arr[i][1]) not in dic:
                dic[(arr[i][0],arr[i][1])]=i+1
        arr=sorted(arr,key=lambda x:x[1])
        lst=[]
        ele=-1
        for i in range(N):
            if arr[i][0]>ele:
                lst.append(dic[(arr[i][0],arr[i][1])])
                ele=arr[i][1]
        lst.sort()
        return lst



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        N = int(input())
        
        
        S=IntArray().Input(N)
        
        
        F=IntArray().Input(N)
        
        obj = Solution()
        res = obj.maxMeetings(N, S, F)
        
        IntArray().Print(res)
        

# } Driver Code Ends