#User function Template for python3
from collections import Counter
class Solution:
    def sameFreq(self, s):
        # code here
        dic=Counter(s)
        lst=list(dic.values())
        st=list(set(dic.values()))
        if len(st)>2:
            return False
        if len(st)==2:
            if lst.count(st[0])>1 and lst.count(st[1])>1:
                return False
            if abs(st[0]-st[1])>1:
                return False
        return True
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	T=int(input())

	for _ in range(T):
		s = input()
		ob = Solution()
		answer = ob.sameFreq(s)
		if answer:
			print(1)
		else:
			print(0)

# } Driver Code Ends