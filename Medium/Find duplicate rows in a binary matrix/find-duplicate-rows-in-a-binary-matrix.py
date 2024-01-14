#User function Template for python3

class Solution:
    def repeatedRows(self, arr, m ,n):
        #code here
        st=set()
        lst=[]
        for i in range(m):
            if tuple(arr[i]) not in st:
                st.add(tuple(arr[i]))
            else:
                lst.append(i)
        return lst


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, m = list(map(int, input().strip().split()))
        
        arr = []
        for i in range(n):
            nums = list(map(int, input().strip().split()))
            arr.append(nums)
        ob = Solution()
        ans = ob.repeatedRows(arr, n, m)
        
        for x in ans:
            print(x, end=" ")
            
        print()
        tc -= 1

# } Driver Code Ends