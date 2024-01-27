#User function Template for python3

class Solution:
    matrix = 'A'
    ans = ""

    def matrixChainOrder(self, p, n):
        # code here
        self.matrix = 'A'
        self.ans = ""
        dp = [[0 for _ in range(n)] for _ in range(n)]
        path = [[0 for _ in range(n)] for _ in range(n)]

        for pair in range(2, n):
            for i in range(1, n - pair + 1):
                j = i + pair - 1
                dp[i][j] = float('inf')
                for k in range(i, j):
                    temp = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                    if temp < dp[i][j]:
                        dp[i][j] = temp
                        path[i][j] = k

        self.dfs(1, n - 1, path)
        return self.ans

    def dfs(self, i, j, path):
        if i == j:
            self.ans += self.matrix
            self.matrix = chr(ord(self.matrix) + 1)
            return

        self.ans += '('
        self.dfs(i, path[i][j], path)
        self.dfs(path[i][j] + 1, j, path)
        self.ans += ')'

#{ 
 # Driver Code Starts

def get(p, n):
    m = [[0] * n for _ in range(n)]
    for i in range(1, n):
        m[i][i] = 0

    for L in range(2, n):
        for i in range(1, n - L + 1):
            m[i][i + L - 1] = float('inf')
            for k in range(i, i + L - 1):
                q = m[i][k] + m[k + 1][i + L - 1] + p[i - 1] * p[k] * p[i + L - 1]
                if q < m[i][i + L - 1]:
                    m[i][i + L - 1] = q

    return m[1][n - 1]

def find(s, p):
    arr = []
    ans = 0
    for t in s:
        if t == '(':
            arr.append((-1, -1))
        elif t == ')':
            b = arr.pop()
            a = arr.pop()
            arr.pop()
            arr.append((a[0], b[1]))
            ans += a[0] * a[1] * b[1]
        else:
            arr.append((p[ord(t) - ord('A')], p[ord(t) - ord('A') + 1]))

    return ans

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    
    ob = Solution()
    result = ob.matrixChainOrder(p, n)
    
    if find(result, p) == get(p, n):
        print("True")
    else:
        print("False")

# } Driver Code Ends