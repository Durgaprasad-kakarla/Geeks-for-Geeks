class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        ele1,ele2,cnt1,cnt2,n=-1,-1,0,0,len(arr)
        for i in range(n):
            if cnt1==0 and arr[i]!=ele2:
                ele1=arr[i]
                cnt1+=1
            elif ele1==arr[i]:
                cnt1+=1
            elif cnt2==0 and ele1!=arr[i]:
                ele2=arr[i]
                cnt2+=1
            elif ele2==arr[i]:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        #     print(ele1,ele2,cnt1,cnt2)
        # print(ele1,ele2)
        cnt1,cnt2=0,0
        for i in range(n):
            if arr[i]==ele1:
                cnt1+=1
            if arr[i]==ele2:
                cnt2+=1
        candidates=[]
        if cnt1>n//3:
            candidates.append(ele1)
        if cnt2>n//3:
            candidates.append(ele2)
        if candidates:
            return candidates
        return [-1]

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
        print(" ".join(map(str, ans)))


if __name__ == "__main__":
    main()

# } Driver Code Ends