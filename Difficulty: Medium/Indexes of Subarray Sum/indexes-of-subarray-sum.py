#User function Template for python3
class Solution:
    def subarraySum(self, arr, target):
        # code here
        n=len(arr)
        sm,dic,indexes=0,{0:0},[]
        for i in range(n):
            sm+=arr[i]
            if sm-target in dic:
                return ([dic[sm-target]+1,i+1])
            if sm not in dic:
                dic[sm]=i+1
        return [-1]


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input().strip())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        d = int(input().strip())
        ob = Solution()
        result = ob.subarraySum(arr, d)
        print(" ".join(map(str, result)))
        tc -= 1
        print("~")

# } Driver Code Ends