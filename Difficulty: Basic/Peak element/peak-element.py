
class Solution:   
    def peakElement(self,arr):
        # Code here
        n=len(arr)
        if n==1:
            return 0
        if arr[0]>arr[1]:
            return 0
        if arr[-1]>arr[-2]:
            return n-1
        l,r=0,n-1
        while l<=r:
            mid=(l+r)//2
            if mid>0 and mid<n-1 and arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            if mid>0 and mid<n-1 and arr[mid-1]>=arr[mid+1]:
                r=mid-1
            else:
                l=mid+1
        return -1
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())  # Read number of test cases
    for _ in range(t):
        # Read input and split it into a list of integers
        arr = list(map(int, input().split()))
        # Create a Solution object and calculate the result

        index = Solution().peakElement(arr)
        n = len(arr)
        flag = False
        if index < 0 or index >= n:
            flag = False
        else:
            if index == 0 and n == 1:
                flag = True
            elif index == 0 and arr[index] > arr[index + 1]:
                flag = True
            elif index == n - 1 and arr[index] > arr[index - 1]:
                flag = True
            elif index > 0 and index < n - 1 and arr[
                    index - 1] < arr[index] and arr[index] > arr[index + 1]:
                flag = True
            else:
                flag = False

        if flag:
            print("true")
        else:
            print("false")
        print("~")

# } Driver Code Ends