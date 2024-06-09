#User function Template for python3
class Solution:

	def matchPairs(self, n, nuts, bolts):
		# code here
		l=['!','#','$','%','&','*','?','@','^']
		new_nuts,new_bolts=[],[]
		for i in range(9):
		    if l[i] in nuts:
		        new_nuts.append(l[i])
		for i in range(n):
		    nuts[i]=new_nuts[i]
		    bolts[i]=new_nuts[i]
		
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        nuts = list(map(str, input().strip().split()))
        bolts = list(map(str, input().strip().split()))
        ob = Solution()
        ob.matchPairs(n, nuts, bolts)
        for x in nuts:
            print(x, end=" ")
        print()
        for x in bolts:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends