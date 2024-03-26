#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3

# return 1 in case of True and 0 in case of False
class Solution:
    def isAdditiveSequence(self, n):
        #code here
        def func(s1,s2,s):
            if not s:
                return True
            st=s1+s2
            astr=str(st)
            if not s.startswith(astr):
                return False
            return func(s2,st,s[len(astr):])
        l=len(n)
        for i in range(1,l):
            for j in range(i+1,l):
                s1,s2=int(n[:i]),int(n[i:j])
                if func(s1,s2,n[j:]):
                    return 1
        return 0

#{ 
 # Driver Code Starts.
        
if __name__ == "__main__":
    sol = Solution()
    t = int(input())
    for _ in range(t):
        s = input()
        print(sol.isAdditiveSequence(s))

# } Driver Code Ends