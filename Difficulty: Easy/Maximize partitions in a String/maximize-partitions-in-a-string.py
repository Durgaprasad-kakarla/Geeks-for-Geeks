class Solution:
    def maxPartitions(self , s):
        # code here
        n=len(s)
        chars=[0]*26
        for i in range(n):
            chars[ord(s[i])-97]=i
        cnt,maxi=0,0
        for i in range(n):
            maxi=max(maxi,chars[ord(s[i])-97])
            if maxi==i:
                cnt+=1
        return (cnt)

#{ 
 # Driver Code Starts
if __name__ == '__main__':
    tc = int(input())

    for _ in range(tc):
        s = input()
        obj = Solution()
        print(obj.maxPartitions(s))
        print("~")

# } Driver Code Ends