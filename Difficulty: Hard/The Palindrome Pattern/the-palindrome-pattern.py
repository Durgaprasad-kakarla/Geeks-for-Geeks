#User function Template for python3

class Solution:
    def pattern (self, arr):
        # code here
        n,m=len(arr),len(arr[0])
        for i in range(n):
            flag=0
            for j in range(m//2):
                if arr[i][j]!=arr[i][m-j-1]:
                    flag=1
                    break
            if flag==0:
                return str(i)+" "+'R'
        for j in range(m):
            flag=0
            for i in range(n//2):
                if arr[i][j]!=arr[n-i-1][j]:
                    flag=1
                    break
            if flag==0:
                return str(j)+" "+'C'
        return -1



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().split()))
        a = list()
        c = 0
        for i in range(0, n):
            X = list()
            for j in range(0, n):
                X.append(arr[c])
                c += 1
            a.append(X)
        ans = ob.pattern(a)
        print(ans)

# } Driver Code Ends