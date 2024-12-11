class Solution:
    def mergeArrays(self, a, b):
        # code here
        n,m=len(a),len(b)
        l,r=n-1,0
        while l>=0 and r<m:
            if a[l]>=b[r]:
                a[l],b[r]=b[r],a[l]
            l-=1
            r+=1
        a.sort()
        b.sort()


#{ 
 # Driver Code Starts
# Input handling and main function
if __name__ == "__main__":
    # Number of test cases
    t = int(input().strip())

    for _ in range(t):
        # Input first array
        a = list(map(int, input().strip().split()))
        # Input second array
        b = list(map(int, input().strip().split()))

        # Create solution object and merge the arrays
        solution = Solution()
        solution.mergeArrays(a, b)

        # Output both arrays in the same line space-separated
        print(" ".join(map(str, a)))
        print(" ".join(map(str, b)))

# } Driver Code Ends