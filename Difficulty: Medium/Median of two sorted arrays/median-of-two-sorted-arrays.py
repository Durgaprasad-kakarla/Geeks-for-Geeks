#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        # code here
        n1,n2=len(arr1),len(arr2)
        if n1>n2:
            return self.sum_of_middle_elements(arr2,arr1)
        l,r=0,n1
        left=(n1+n2+1)//2
        n=n1+n2
        while l<=r:
            mid1=(l+r)//2
            mid2=left-mid1
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
                if n&1==1:
                    return l1+l2
                else:
                    return (max(l1,l2)+min(r1,r2))
            elif l1>r2:
                r=mid1-1
            else:
                l=mid1+1
        return -1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

input = sys.stdin.read


def main():
    input_lines = input().strip().split("\n")
    t = int(input_lines[0])

    index = 1
    results = []
    while t > 0:
        arr = list(map(int, input_lines[index].strip().split()))
        brr = list(map(int, input_lines[index + 1].strip().split()))
        index += 2

        solution = Solution()
        res = solution.sum_of_middle_elements(arr, brr)
        results.append(res)

        t -= 1

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

# } Driver Code Ends