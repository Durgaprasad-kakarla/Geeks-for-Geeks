#User function Template for python3
class Solution:
	def printString(self, s, ch, count):
		# code here
		n=len(s)
		for i in range(n):
		    if s[i]==ch:
		        count-=1
		    if count==0:
		        return s[i+1:]
		return ''


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()
        ch = input()[0]
        count = int(input())
        ob = Solution()
        answer = ob.printString(s, ch, count)

        print(answer)

# } Driver Code Ends