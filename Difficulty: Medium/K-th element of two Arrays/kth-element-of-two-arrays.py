#User function Template for python3

class Solution:
    def kthElement(self, k, arr1, arr2):
        n1,n2=len(arr1),len(arr2)
        if n1>n2:
            return self.kthElement(k,arr2,arr1)
        left=k-1
        l,r=0,n1
        while l<=r:
            mid1=(l+r)//2
            mid2=left-mid1
            if mid2<0:
                r=mid1-1
                continue
            if mid2>n2:
                l=mid1+1
                continue
            l1,l2,r1,r2=-float('inf'),-float('inf'),float('inf'),float('inf')
            if mid1<n1:
                r1=arr1[mid1]
            if mid2<n2:
                r2=arr2[mid2]
            if mid1-1>=0:
                l1=arr1[mid1-1]
            if mid2-1>=0:
                l2=arr2[mid2-1]
            if l1<=r2 and l2<=r1:
                return min(r1,r2)
            elif l1>r2:
                r=mid1-1
            else:
                l=mid1+1
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