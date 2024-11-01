#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        n=len(arr)
        arr.sort()
        lst=[]
        l,r=0,n-1
        while l<=r:
            lst.append(arr[l])
            lst.append(arr[r])
            l+=1
            r-=1
        if n&1==1:
            lst.pop()
        sm=0
        for i in range(1,n):
            sm+=abs(lst[i]-lst[i-1])
        sm+=abs(lst[0]-lst[-1])
        return sm

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends