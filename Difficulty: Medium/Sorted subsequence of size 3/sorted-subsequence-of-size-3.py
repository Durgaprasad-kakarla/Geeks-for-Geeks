#User function Template for python3



class Solution:
    def find3Numbers(self, arr):
        # Code Here
        n=len(arr)
        smaller=[-1]*n
        stack=[]
        for i in range(n):
            while stack and stack[-1]>=arr[i]:
                stack.pop()
            if stack:
                smaller[i]=stack[-1]
            stack.append(arr[i])
        stack=[]
        greater=[-1]*n
        for i in range(n-1,-1,-1):
            while stack and stack[-1]<=arr[i]:
                stack.pop()
            if stack:
                greater[i]=stack[-1]
            stack.append(arr[i])
        # print(smaller,greater)
        # return [-1,-1,-1]
        for i in range(1,n-1):
            if smaller[i]!=-1 and greater[i]!=-1:
                return [smaller[i],arr[i],greater[i]]
        return []
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def isSubSequence(v1, v2):
    m = len(v2)
    n = len(v1)
    j = 0  # For index of v2
    # Traverse v1 and v2
    for i in range(n):
        if j < m and v1[i] == v2[j]:
            j += 1
    return j == m


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        n = len(arr)
        obj = Solution()
        res = obj.find3Numbers(arr)
        if len(res) != 0 and len(res) != 3:
            print(-1)
        else:
            if not res:
                print(0)
            elif res[0] < res[1] < res[2] and isSubSequence(arr, res):
                print(1)
            else:
                print(-1)

# } Driver Code Ends