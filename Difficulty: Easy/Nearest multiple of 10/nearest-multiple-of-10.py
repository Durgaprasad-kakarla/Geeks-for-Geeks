#User function Template for python3

class Solution:
    def roundToNearest (self, st) : 
        #Complete the function
        n=len(st)
        st=list(st)
        if len(st)==1:
            if st[0]<='5':
                return '0'
            else:
                return '10'
        last=st[n-1]
        flag=0
        if last=='0':
            return "".join(st)
        if st[n-2]=='0':
            if last<='5':
                st[n-1]='0'
            else:
                st[n-2]='1'
                st[n-1]='0'
        else:
            if last<='5':
                st[n-1]='0'
            else:
                flag=0
                for i in range(n-2,-1,-1):
                    if st[i]=='9':
                        st[i]='0'
                    else:
                        st[i]=str(int(st[i])+1)
                        flag=1
                        break
                if flag==0:
                    st.insert(0,'1')
                st[n-1]='0'
        return "".join(st)
                    


#{ 
 # Driver Code Starts
#Initial Template for Python 3
for _ in range(0, int(input())):
    num_str = input()
    ob = Solution()
    res = ob.roundToNearest(num_str)
    print(res)

# } Driver Code Ends