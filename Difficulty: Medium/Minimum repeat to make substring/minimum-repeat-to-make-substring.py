#User function Template for python3

class Solution:
    def minRepeats(self, s1, s2):
        def lps_of_a_string(s):
            n=len(s)
            lps=[0]*n
            i,length=1,0
            while i<n:
                if s[i]==s[length]:
                    lps[i]=length+1
                    length+=1
                    i+=1
                else:
                    if length!=0:
                        length=lps[length-1]
                    else:
                        lps[i]=0
                        i+=1
            return lps
        
        def Knuth_Morris_Pratt_Algorithm(txt,pattern):
            n,m=len(txt),len(pattern)
            lps=lps_of_a_string(pattern)
            i,j,cnt=0,0,0
            while i<n:
                if txt[i]==pattern[j]:
                    i+=1
                    j+=1
                if j==m:
                    cnt+=1
                    j=lps[j-1]
                elif i<n and txt[i]!=pattern[j]:
                    if j==0:
                        i+=1
                    else:
                        j=lps[j-1]
            return cnt
        # code here 
        n,m=len(s1),len(s2)
        s=s1
        cnt=1
        if n<m:
            if m%n!=0:
                cnt+=m//n
            else:
                cnt+=m//n-1
            s1=s*cnt
        if Knuth_Morris_Pratt_Algorithm(s1,s2): 
            return cnt
        s1+=s
        cnt+=1
        if Knuth_Morris_Pratt_Algorithm(s1,s2):
            return cnt
        return -1
    
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        A = input()
        B = input()

        ob = Solution()
        print(ob.minRepeats(A, B))

# } Driver Code Ends