#User function Template for python3
class Solution:
	def binaryNextNumber(self, s):
		# code here
		s=list(s)
	    n=len(s)
	    flag=0
	    for i in range(n-1,-1,-1):
	        if s[i]=='0':
	            s[i]='1'
	            flag=1
	            break
	        else:
	            s[i]='0'
	    while s and s[0]=='0':
	        s.pop(0)
	    s="".join(s)
	    if flag==0:
	        return '1'+'0'*n
	    else:
	        return s


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        S = input()
        ob = Solution()
        ans = ob.binaryNextNumber(S)
        print(ans)

# } Driver Code Ends