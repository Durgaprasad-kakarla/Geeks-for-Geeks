#User function Template for python3
class Solution:
    def isValid(self, s):
        #code here
        s=s.split('.')
        for i in s:
            if int(i)>255:
                return False
        return True


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends