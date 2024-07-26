#User function Template for python3
class Solution:
    def kPangram(self,string, k):
        string=string.replace(' ','')
        n=len(string)
        st=set(string)
        if n>=26 and 26-len(st)<=k:
            return True
        return False
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())

    for tcs in range(T):
        string = input()
        K = int(input())
        ob = Solution()
        a = ob.kPangram(string, K)
        if a:
            print("true")
        else:
            print("false")

# } Driver Code Ends