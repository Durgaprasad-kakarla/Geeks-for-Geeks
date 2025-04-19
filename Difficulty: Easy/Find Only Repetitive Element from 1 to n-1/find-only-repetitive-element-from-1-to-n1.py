#User function Template for python3
class Solution:
    def findDuplicate(self, arr):
        #code here
        n=len(arr)
        dic={}
        for i in range(n):
            if arr[i] in dic:
                return arr[i]
            dic[arr[i]]=1
        return -1
        

#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().strip().split()))

        ob = Solution()
        print(ob.findDuplicate(arr))
        print("~")

# } Driver Code Ends