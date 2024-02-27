#User function Template for python3

class Solution:
    def game_with_number (self, arr,  n) : 
        #Complete the function
        new_arr=[0]*n
        new_arr[n-1]=arr[n-1]
        for i in range(n-1):
            new_arr[i]=arr[i]|arr[i+1]
        return new_arr

#{ 
 # Driver Code Starts

#Initial Template for Python 3


for _ in range(0,int(input())):
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.game_with_number(arr, n);
    print(*res)




# } Driver Code Ends