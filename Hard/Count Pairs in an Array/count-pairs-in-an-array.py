#User function Template for python3

class Solution:    
    def countPairs(self,arr, n): 
         # Your code goes here
        def merge(arr,l,mid,r):
            low,high=l,mid+1
            lst=[]
            cnt=0
            while low<=mid:
                while high<=r and arr[low]>arr[high]:
                    high+=1
                cnt+=(high-(mid+1))
                low+=1
            low,high=l,mid+1
            while low<=mid and high<=r:
                if arr[low]<=arr[high]:
                    lst.append(arr[low])
                    low+=1
                else:
                    lst.append(arr[high])
                    high+=1
            while low<=mid:
                lst.append(arr[low])
                low+=1
            while high<=r:
                lst.append(arr[high])
                high+=1
            for i in range(l,r+1):
                arr[i]=lst[i-l]
            return cnt
        def mergesort(arr,l,r):
            if l>=r:
                return 0
            cnt=0
            mid=(l+r)//2
            cnt+=mergesort(arr,l,mid)
            cnt+=mergesort(arr,mid+1,r)
            cnt+=merge(arr,l,mid,r)
            return cnt
        for i in range(n):
            arr[i]=i*arr[i]
        cnt=mergesort(arr,0,n-1)
        return cnt
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob= Solution()
        print(ob.countPairs(a, n))

        T -= 1


if __name__ == "__main__":
    main()
    
# } Driver Code Ends