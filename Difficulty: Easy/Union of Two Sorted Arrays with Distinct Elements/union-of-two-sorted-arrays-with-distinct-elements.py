#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    #Function to return a list containing the union of the two arrays.
    def findUnion(self,a,b):
        # code here 
        i,j,n,m=0,0,len(a),len(b)
        lst=[]
        while i<n and j<m:
            if a[i]<b[j]:
                lst.append(a[i])
                i+=1
            elif a[i]>b[j]:
                lst.append(b[j])
                j+=1
            else:
                lst.append(a[i])
                i+=1
                j+=1
        while i<n:
            lst.append(a[i])
            i+=1
        while j<m:
            lst.append(b[j])
            j+=1
        return lst

#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
        ob = Solution()
        li = ob.findUnion(a, b)
        for val in li:
            print(val, end=' ')
        print()
        print("~")
# } Driver Code Ends