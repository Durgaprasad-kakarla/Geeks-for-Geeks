
from typing import List


class Solution:
    def maxTip(self, n : int, x : int, y : int, arr : List[int], brr : List[int]) -> int:
        # code here
        crr=[]
        for i in range(n):
            if arr[i]>brr[i]:
                crr.append([arr[i]-brr[i],0,i])
            elif arr[i]==brr[i]:
                crr.append([0,0,i])
            else:
                crr.append([brr[i]-arr[i],1,i])
        crr.sort(reverse=True)
        tot=0
        for i in range(n):
            diff,l,ind=crr[i]
            if l==0:
                x-=1
                if x>=0:
                    tot+=(arr[ind])
                else:
                    tot+=(brr[ind])
            else:
                y-=1
                if y>=0:
                    tot+=(brr[ind])
                else:
                    tot+=(arr[ind])
        return tot
                
        



#{ 
 # Driver Code Starts
class IntArray:

    def __init__(self) -> None:
        pass

    def Input(self, n):
        arr = [int(i) for i in input().strip().split()]  #array input
        return arr

    def Print(self, arr):
        for i in arr:
            print(i, end=" ")
        print()


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        x = int(input())

        y = int(input())

        arr = IntArray().Input(n)

        brr = IntArray().Input(n)

        obj = Solution()
        res = obj.maxTip(n, x, y, arr, brr)

        print(res)

# } Driver Code Ends