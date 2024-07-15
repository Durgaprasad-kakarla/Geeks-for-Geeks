#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def smallestNumber(self, s, d):
        # code here
        if d*9<s:
            return -1
        ans=[]
        def func(d,x,temp):
            if d==0:
                if x==s:
                   ans.append(temp)
                   return True
                return False
            for i in range(10):
                if x>0 and i==0:
                    if func(d-1,i+x,temp+str(0)):
                        return True
                if i+x<=s and i>0:
                    if func(d-1,i+x,temp+str(i)):
                        return True
            return False
        temp=''
        func(d,0,temp)
        return ans[0]
        
        
        


#{ 
 # Driver Code Starts.
# Position this line where user code will be pasted.

import sys
import math
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    s = int(data[index])
    d = int(data[index + 1])
    index += 2
    ob = Solution()
    print(ob.smallestNumber(s, d))

# } Driver Code Ends