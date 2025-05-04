#User function Template for python3

class Solution:
    def findSubString(self, s):
        # code here
        n=len(s)
        dic,k,start,mini={},len(set(list(s))),0,float('inf')
        for i in range(n):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
            while start<n and len(dic)>=k:
                mini=min(mini,i-start+1)
                dic[s[start]]-=1
                if dic[s[start]]==0:
                    del dic[s[start]]
                start+=1
        return mini
            
        
    
    # aabcbcdbca
    #   s      i
#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    T = int(input())
    while (T > 0):
        str = input()
        ob = Solution()
        print(ob.findSubString(str))

        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends