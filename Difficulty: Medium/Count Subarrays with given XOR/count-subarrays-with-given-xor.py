class Solution:
    def subarrayXor(self, arr, k):
        # code here
        dic={0:1}
        pref=cnt=0
        n=len(arr)
        for i in range(n):
            pref^=arr[i]
            if pref^k in dic:
                cnt+=dic[pref^k]
            if pref in dic:
                dic[pref]+=1
            else:
                dic[pref]=1
        return cnt


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends