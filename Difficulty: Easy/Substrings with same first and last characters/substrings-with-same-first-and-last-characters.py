from collections import Counter
class Solution:
	def countSubstring(self, s):
		# code here
		dic=Counter(s)
        tot=0
        for i in dic:
            tot+=(dic[i]*(dic[i]+1))//2
        return tot

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.countSubstring(s)

        print(answer)
        print("~")

# } Driver Code Ends