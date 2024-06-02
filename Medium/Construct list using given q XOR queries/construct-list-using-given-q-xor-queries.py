
from typing import List

class Solution:
    def constructList(self, q : int, queries : List[List[int]]) -> List[int]:
        # code here
        lst=[0]
        for op,x in queries:
            if op==1:
                lst[-1]=lst[-1]^x
            else:
                lst.append(0)
        #     print(lst)
        # print(lst)
        n=len(lst)
        pref=[0]*(n)
        pref[-1]=lst[-1]
        for i in range(n-2,-1,-1):
            pref[i]=pref[i+1]^lst[i]
        # print(pref)
        lst[0]=pref[0]
        x=1
        for op,ele in queries:
            if op==0:
                lst[x]=pref[x]^ele
                x+=1
        return sorted(lst)
                
        



#{ 
 # Driver Code Starts
class IntMatrix:

    def __init__(self) -> None:
        pass

    def Input(self, n, m):
        matrix = []
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix

    def Print(self, arr):
        for i in arr:
            for j in i:
                print(j, end=" ")
            print()


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

        q = int(input())

        queries = IntMatrix().Input(q, 2)

        obj = Solution()
        res = obj.constructList(q, queries)

        IntArray().Print(res)

# } Driver Code Ends