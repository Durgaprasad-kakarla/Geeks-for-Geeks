
class Solution:
    def countNumberswith4(self, n : int) -> int:
        # code here
        cnt=0
        for i in range(1,n+1):
            st=set(str(i))
            if '4' in st:
                cnt+=1
        return cnt
        



#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):

        n = int(input())

        obj = Solution()
        res = obj.countNumberswith4(n)

        print(res)

# } Driver Code Ends