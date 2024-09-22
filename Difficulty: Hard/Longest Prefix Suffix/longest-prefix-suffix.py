#User function Template for python3

class Solution:
	def lps(self, s):
		# code here
        n=len(s)
        i,l=1,0
        lps=[0]*n
        while i<n:
            if s[i]==s[l]:
                lps[i]=l+1
                l+=1
                i+=1
            else:
                if l!=0:
                    l=lps[l-1]
                else:
                    lps[i]=0
                    i+=1
        return lps[-1]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.lps(s)
        print(answer)

# } Driver Code Ends