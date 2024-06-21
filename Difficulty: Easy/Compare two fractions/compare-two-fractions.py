#User function Template for python3


class Solution:
    def compareFrac (self, st):
        st=st.replace(" ","")
        st=st.split(",")
        if eval(st[0])>eval(st[1]):
            return st[0]
        elif eval(st[0])<eval(st[1]):
            return st[1]
        else:
            return 'equal'
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3
import re

if __name__ == '__main__':
    ob = Solution()
    t = int(input())
    for _ in range(t):
        str = input()
        print(ob.compareFrac(str))

# } Driver Code Ends