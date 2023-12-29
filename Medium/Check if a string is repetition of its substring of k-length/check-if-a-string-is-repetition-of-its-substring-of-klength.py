#User function Template for python3
class Solution:
	def kSubstrConcat(self, n, s, k):
		# Your Code Here
		if n%k!=0:
		    return 0
		else:
		    dic={}
		    for i in range(0,n,k):
		        if s[i:i+k] in dic:
		            dic[s[i:i+k]]+=1
		        else:
		            dic[s[i:i+k]]=1
		    if len(dic)==1:
		        return 1
            if len(dic)==2:
                lst=dic.values()
                if 1 in lst:
                    return 1
                return 0
            else:
                return 0
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
	t = int (input ())
	for tc in range (t):
		n = int (input ())
		s = input()
		k = int(input())
		ob = Solution()
		print(ob.kSubstrConcat(n,s,k))

# } Driver Code Ends