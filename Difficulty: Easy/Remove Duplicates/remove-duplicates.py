#User function Template for python3
class Solution:
	def removeDups(self, s):
		# code here
		st=set()
		stri=''
		for i in range(len(s)):
		    if s[i] not in st:
		        stri+=s[i]
		        st.add(s[i])
		return stri


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)

# } Driver Code Ends