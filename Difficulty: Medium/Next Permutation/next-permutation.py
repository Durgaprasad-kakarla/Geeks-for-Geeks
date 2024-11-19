#User function Template for python3

class Solution:
    def nextPermutation(self, arr):
        # code here
        n=len(arr)
        ind=-1
        for i in range(n-2,-1,-1):
            if arr[i]<arr[i+1]:
                ind=i
                break
        # print(ind)
        if ind==-1:
            for i in range(n//2):
                arr[i],arr[n-i-1]=arr[n-i-1],arr[i]
        else:
            for i in range(n-1,-1,-1):
                if arr[ind]<arr[i]:
                    arr[ind],arr[i]=arr[i],arr[ind]
                    break
            l,r=ind+1,n-1
            while l<r:
                arr[l],arr[r]=arr[r],arr[l]
                l+=1
                r-=1
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        N = len(arr)
        for i in range(N):
            arr[i] = int(arr[i])

        ob = Solution()
        ob.nextPermutation(arr)
        for i in range(N):
            print(arr[i], end=" ")
        print()

# } Driver Code Ends