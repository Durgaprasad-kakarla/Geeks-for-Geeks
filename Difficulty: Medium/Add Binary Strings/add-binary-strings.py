#User function Template for python3
class Solution:
	def addBinary(self, s1, s2):
		# code here
		n,m=len(s1),len(s2)
		i,j=n-1,m-1
		s=''
		carry=0
		while i>=0 or j>=0 or carry>0:
		    cnt=0
		    if i>=0:
		        if s1[i]=='1':
		            cnt+=1
		        i-=1
		    if j>=0:
		        if s2[j]=='1':
		            cnt+=1
		        j-=1
		    if carry>0:
		        cnt+=1
		    if cnt==0:
		        s+='0'
		    elif cnt==1:
		        s+='1'
		        carry=0
		    elif cnt==2:
		        s+='0'
		        carry=1
		    else:
		        s+='1'
		        carry=1
	    return s[::-1].lstrip('0')


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        a = input().strip()
        b = input().strip()
        ob = Solution()
        answer = ob.addBinary(a, b)

        print(answer)
        print("~")

# } Driver Code Ends