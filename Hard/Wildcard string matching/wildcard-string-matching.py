#User function Template for python3

class Solution:
    def match(self,p, s):
        # code here
        i = j = 0  
        back_j = -1  
        match_i = 0   
        m = len(s)
        n = len(p)
        while i < m:
            if j < n and (s[i] == p[j] or p[j] == '?'):  
                i += 1
                j += 1
            elif j < n and p[j] == '*':  
                back_j = j  
                match_i = i  
                j += 1  
            elif back_j != -1:  
                j = back_j + 1
                match_i += 1  
                i = match_i
            else:  
                return False
        return list(p[j:]).count('*') == len(p[j:])
                
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        wild = input()
        pattern = input()
        
        ob = Solution()
        if(ob.match(wild, pattern)):
            print("Yes")
        else:
            print("No")
# } Driver Code Ends