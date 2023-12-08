#User function Template for python3
import math
class Solution:
    def smithNum(self, n):
        # code here 
        def prime(n):
            if n<2:
                return False
            for i in range(2,int(math.sqrt(n))+1):
                if n%i==0:
                    return False
            return True
        lst=[]
        for i in range(2,n):
            if n%i==0 and prime(i):
                lst.append(i)
        tot=0
        def sumofdigits(n):
            sm=0
            while n!=0:
                rem=(n%10)
                sm+=rem
                n=n//10
            return sm
        num=n
        prod=1
        for i in lst:
            cnt=0
            while n>1 and n%i==0:
                n=n//i
                cnt+=1
            prod*=(i**cnt)
            tot+=(sumofdigits(i)*cnt)
        return 1 if tot==sumofdigits(num) and num==prod else 0
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n=int(input())
        
        ob = Solution()
        print(ob.smithNum(n))
# } Driver Code Ends