#User function Template for python3
class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        #code here
        citations.sort()
        n=len(citations)
        # def binary_search(arr,ele):
        #     n=len(arr)
        #     l,r=0,n-1
        #     while l<=r:
        #         mid=(l+r)//2
        #         if arr[mid]<ele:
        #             l=mid+1
        #         else:
        #             r=mid-1
        #     return n-l
        maxi=0
        i,j=1,0
        while i<n+1 and j<n:
            if citations[j]==0:
                j+=1
                continue
            elif i<=citations[j]:
                if (n-j)>=i:
                    maxi=max(maxi,i)
                    i+=1
                else:
                    j+=1
            else:
                j+=1
        return maxi


#{ 
 # Driver Code Starts
# Initial Template for Python 3

# Main
if __name__ == '__main__':
    t = int(input())
    while t > 0:
        t -= 1
        arr = [int(x) for x in input().strip().split()]

        ob = Solution()
        result = ob.hIndex(arr)

        print(result)
        print("~")

# } Driver Code Ends