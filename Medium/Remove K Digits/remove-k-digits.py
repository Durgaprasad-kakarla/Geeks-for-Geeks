#User function Template for python3

class Solution:

    def removeKdigits(self, num, k):
        # code here
        stack=[]
        n=len(num)
        for i in range(n):
            while stack and stack[-1]>num[i] and k>0:
                stack.pop(-1)
                k-=1
            if not stack and num[i]=='0':
                continue
            else:
                stack.append(num[i])
        if k>0:
            if len(stack)<=k:
                return 0
            return "".join(stack[:-(k)])
        else:
            return "".join(stack)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends