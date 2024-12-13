#User function Template for python3

class Solution:
    def findMin(self, arr):
        #complete the function here
        n=len(arr)
        l,r=0,n-1
        mini=float('inf')
        while l<=r:
            while l+1<r and arr[l]==arr[l+1]:
                l+=1
            while r-1>l and arr[r]==arr[r-1]:
                r-=1
            mid=(l+r)//2
            mini=min(mini,arr[mid])
            if arr[l]>arr[mid]:
                if arr[l]>=arr[r]:
                    r=mid-1
                else:
                    l=mid+1
            else:
                if arr[l]>=arr[r]:
                    l=mid+1
                else:
                    r=mid-1
        return mini

#{ 
 # Driver Code Starts
def main():
    T = int(input())

    while T > 0:
        a = list(map(
            int,
            input().strip().split()))  # Convert input to list of integers
        print(Solution().findMin(a))  # Call findMin with the array 'a'
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends