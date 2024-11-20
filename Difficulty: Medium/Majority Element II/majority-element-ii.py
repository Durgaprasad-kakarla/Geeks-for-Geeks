class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n=len(arr)
        ele1,ele2,cnt1,cnt2=-1,-1,0,0
        for i in range(n):
            if cnt1==0 and ele2!=arr[i]:
                ele1=arr[i]
                cnt1+=1
            elif ele1==arr[i]:
                cnt1+=1
            elif cnt2==0:
                ele2=arr[i]
                cnt2+=1
            elif ele2==arr[i]:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        cnt1,cnt2=0,0
        for i in range(n):
            if ele1==arr[i]:
                cnt1+=1
            if ele2==arr[i]:
                cnt2+=1
        lst=[]
        if cnt1>n//3:
            lst.append(ele1)
        if cnt2>n//3:
            lst.append(ele2)
        return sorted(lst)
                


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input().strip())
    for _ in range(t):
        s = input().strip()
        nums = list(map(int, s.split()))
        ob = Solution()
        ans = ob.findMajority(nums)
        if not ans:
            print("[]")
        else:
            print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends