#User function Template for python3
class Solution:
	def twoSum(self, arr, target):
		# code here
		st,n=set(),len(arr)
		for i in range(n):
		    if target-arr[i] in st:
		        return True
		    st.add(arr[i])
		return False


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#Initial Template for Python 3


def main():
    T = int(input())
    while T > 0:
        x = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.twoSum(arr, x)
        if ans:
            print("true")
        else:
            print("false")
        T -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends