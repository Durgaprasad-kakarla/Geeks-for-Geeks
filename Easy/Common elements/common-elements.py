#User function Template for python3

class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        # your code here
        def func(a,b):
            lst=[]
            i,j,n,m=0,0,len(a),len(b)
            while i<n and j<m:
                if a[i]>b[j]:
                    j+=1
                elif a[i]<b[j]:
                    i+=1
                else:
                    if lst and lst[-1]!=a[i]:
                        lst.append(a[i])
                    if not lst:
                        lst.append(a[i])
                    i+=1
                    j+=1
            return lst
        lst=func(A,B)
        final=func(lst,C)
        return final
#{ 
 # Driver Code Starts
#Initial Template for Python 3


t = int (input ())
for tc in range (t):
    n1, n2, n3 = list(map(int,input().split()))
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    C = list(map(int,input().split()))
    
    ob = Solution()
    
    res = ob.commonElements (A, B, C, n1, n2, n3)
    
    if len (res) == 0:
        print (-1)
    else:
        for i in range (len (res)):
            print (res[i], end=" ")
        print ()

# } Driver Code Ends