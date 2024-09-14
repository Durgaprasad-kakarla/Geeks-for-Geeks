#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        n=len(arr)
        pos,neg=[],[]
        for i in range(n):
            if arr[i]>=0:
                pos.append(arr[i])
            elif arr[i]<0:
                neg.append(arr[i])
        i=0
        while pos and neg:
            arr[i]=pos.pop(0)
            i+=1
            arr[i]=neg.pop(0)
            i+=1
        while pos:
            arr[i]=pos.pop(0)
            i+=1
        while neg:
            arr[i]=neg.pop(0)
            i+=1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends