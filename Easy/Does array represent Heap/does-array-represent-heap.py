
class Solution:
    def isMaxHeap(self,arr,n):
        # Your code goes here  
        i=0
        x,y=1,2
        while True:
            if x<n:
                if arr[i]<arr[x]:
                    return False
            else:
                break
            if y<n:
                if arr[i]<arr[y]:
                    return False
            else:
                break
            i+=1
            x=y+1
            y=x+1
        return True



#{ 
 # Driver Code Starts
if __name__ =='__main__':
    t= int(input())
    for tcs in range(t):
        n=int(input())
        arr=[int(x) for x in input().split()]
        ob=Solution()
        print(int(ob.isMaxHeap(arr,n)))
# } Driver Code Ends