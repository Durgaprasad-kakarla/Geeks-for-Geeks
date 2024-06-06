#User function Template for python3

def max_sum(a,n):
    #code here
    sm=sum(a)
    curr=0
    for i in range(n):
        curr+=arr[i]*i
    maxi=curr
    for i in range(1,n):
        temp=curr-(sm-arr[i-1])+arr[i-1]*(n-1)
        maxi=max(maxi,temp)
        curr=temp
    return maxi
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        print(max_sum(arr, n))

# } Driver Code Ends