class Solution:
    def canSplit(self, arr):
        #code here
        sm,n=sum(arr),len(arr)
        if sm%2!=0:
            return False
        pref=0
        for i in range(n):
            pref+=arr[i]
            if pref==sm//2:
                return True
        return False


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")

# } Driver Code Ends