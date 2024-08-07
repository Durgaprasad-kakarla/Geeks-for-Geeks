#User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        i,j=0,0
        m,n=len(arr1),len(arr2)
        cnt=1
        while i<m and j<n:
            if arr1[i]<arr2[j]:
                if cnt==k:
                    return arr1[i]
                i+=1
            else:
                if cnt==k:
                    return arr2[j]
                j+=1
            cnt+=1
        while i<m:
            if cnt==k:
                return arr1[i]
            cnt+=1
            i+=1
        while j<n:
            if cnt==k:
                return arr2[j]
            cnt+=1
            j+=1
        return -1
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):

        k = int(input())
        a = [int(x) for x in input().strip().split()]
        b = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.kthElement(k, a, b))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends