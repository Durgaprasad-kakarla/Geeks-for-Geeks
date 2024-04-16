from typing import List
class Solution:
    def minimizeDifference(self, n : int, k : int, arr : List[int]) -> int:
        # code here
        prefmax=[0]*n
        prefmin=[0]*n
        prefmax[n-1]=arr[n-1]
        prefmin[n-1]=arr[n-1]
        for i in range(n-2,-1,-1):
            prefmax[i]=max(arr[i],prefmax[i+1])
            prefmin[i]=min(arr[i],prefmin[i+1])
        mindiff=prefmax[k]-prefmin[k]
        mini,maxi=arr[0],arr[0]
        for i in range(1,n-k):
            mindiff=min(mindiff,max(maxi,prefmax[i+k])-min(mini,prefmin[i+k]))
            mini=min(mini,arr[i])
            maxi=max(maxi,arr[i])
        mindiff=min(maxi-mini,mindiff)
        return mindiff
            


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
        
        n = int(input())
        
        
        k = int(input())
        
        
        arr=IntArray().Input(n)
        
        obj = Solution()
        res = obj.minimizeDifference(n, k, arr)
        
        print(res)
        

# } Driver Code Ends