#User function Template for python3

class Solution:
    def sumXOR (self, arr, n) : 
        #Complete the function
        sm=0
        for i in range(32):
            setbits,unsetbits=0,0
            for j in range(n):
                if arr[j]&(1<<i)!=0:
                    setbits+=1
                else:
                    unsetbits+=1
            sm+=(setbits*unsetbits)*(1<<i)
        return sm
        ''' Time Complexity--O(n)
            Space Complexity--O(1)'''



#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    
    n = int(input())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    res = ob.sumXOR(arr, n)
    print(res)


# } Driver Code Ends