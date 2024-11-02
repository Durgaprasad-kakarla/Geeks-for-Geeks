#User function Template for python3
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        st=set()
        n=len(arr)
        k+=1
        for i in range(k):
            if arr[i] in st:
                return True
            st.add(arr[i])
        for i in range(k,n):
            st.remove(arr[i-k])
            if arr[i] in st:
                return True
            st.add(arr[i])
        return False

#{ 
 # Driver Code Starts
# Initial Template for Python 3
# Position this line where user code will be pasted.
# Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        arr = list(map(int, input().split()))
        k = int(input())
        ob = Solution()
        res = ob.checkDuplicatesWithinK(arr, k)
        if res:
            print("true")
        else:
            print("false")
        # print(res)
        print("~")
        t -= 1
# } Driver Code Ends