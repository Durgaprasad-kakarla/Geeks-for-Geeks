class Solution:
    def shuffleArray(self, arr, n):
        # Your code goes here
        lst1,lst2=[],[]
        for i in range(n//2):
            lst1.append(arr[i])
        for i in range(n//2,n):
            lst2.append(arr[i])
        x=0
        for i in range(n//2):
            arr[x]=lst1[i]
            arr[x+1]=lst2[i]
            x+=2
#{ 
 # Driver Code Starts
if __name__ == '__main__': 
    
    t=int(input())
    for _ in range(0,t):
        n=int(input())
        a = list(map(int,input().split()))
        ob = Solution()
        ob.shuffleArray(a,n)
        print(*a)
# } Driver Code Ends