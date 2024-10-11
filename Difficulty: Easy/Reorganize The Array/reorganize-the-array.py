#{ 
 # Driver Code Starts

# } Driver Code Ends
class Solution:
    def rearrange(self, arr):
        #Code here
        n=len(arr)
        for i in range(n):
            if arr[i]==-1:
                continue
            else:
                ele=arr[i]
                while ele!=arr[ele]:
                    if arr[ele]==-1:
                        arr[i],arr[ele]=arr[ele],arr[i]
                        break
                    arr[i],arr[ele]=arr[ele],arr[i]
                    ele=arr[i]
        return arr
        

#{ 
 # Driver Code Starts.
def main():
    t = int(input())
    for _ in range(t):
        input_str = input()
        arr = list(map(int, input_str.split()))
        solution = Solution()
        ans = solution.rearrange(arr)
        print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()
# } Driver Code Ends