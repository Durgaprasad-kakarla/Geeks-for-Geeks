#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends

# from typing import List


class Solution:
    def rotateDelete(self,  arr):
        # code here
        n=len(arr)
        k=1
        while len(arr)>1:
            arr.insert(0,arr.pop())
            index=len(arr)-k
            if index<0:
                index=0
            arr.pop(index)
            k+=1
        return arr[0]
        
        


#{ 
 # Driver Code Starts.
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        ob = Solution()
        res = ob.rotateDelete(arr)
        print(res)
        t -= 1


# } Driver Code Ends