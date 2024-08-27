class Solution:
    def findMaxDiff(self, arr):
        # code here
        n=len(arr)
        ls=[0]*n
        stack=[]
        for i in range(n):
            while stack and stack[-1]>=arr[i]:
                stack.pop()
            if stack:
                ls[i]=stack[-1]
            stack.append(arr[i])
        # print(ls)
        rs=[0]*n
        maxi=0
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and stack[-1]>=arr[i]:
                stack.pop()
            if stack:
                rs[i]=stack[-1]
            maxi=max(abs(ls[i]-rs[i]),maxi)
            stack.append(arr[i])
        # print(rs)
        return maxi


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.findMaxDiff(arr))

# } Driver Code Ends