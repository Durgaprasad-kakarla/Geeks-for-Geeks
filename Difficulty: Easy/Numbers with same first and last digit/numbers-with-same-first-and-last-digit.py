#User function Template for python3
class Solution:
    def numbersInRange (self,l,r):
        # code here 
        def func(ind,flag,first,last,arr,n):
            # print(ind,flag,first,last)
            if ind==n:
                if first==last:
                    # print(ind,flag,first,last)
                    return 1
                return 0
            if dp[ind][flag][first][last]!=-1:
                return dp[ind][flag][first][last]
            limit=9
            if flag==0:
                limit=arr[ind]
            cnt=0
            for i in range(limit+1):
                if arr[ind]==i:
                    if first==0:
                        cnt+=(func(ind+1,flag,i,i,arr,n))
                    else:
                        cnt+=func(ind+1,flag,first,i,arr,n)
                else:
                    if first==0:
                        cnt += (func(ind + 1, 1, i, i, arr, n))
                    else:
                        cnt += func(ind + 1, 1, first, i,arr, n)
            dp[ind][flag][first][last]=cnt
            return cnt
        if l>r:
            return 0
        l1,r1=str(l-1),str(r)
        arr1=[]
        arr2=[]
        for i in range(len(l1)):
            arr1.append(int(l1[i]))
        for i in range(len(r1)):
            arr2.append(int(r1[i]))
        # print(arr1,arr2)
        dp=[[[[-1 for _ in range(10)] for _ in range(10)] for _ in range(2)] for _ in range(19)]
        ans2=func(0,0,0,0,arr2,len(arr2))-1
        dp=[[[[-1 for _ in range(10)] for _ in range(10)] for _ in range(2)] for _ in range(19)]
        ans1=func(0,0,0,0,arr1,len(arr1))-1
        # print(ans1,ans2,ans2-ans1)
        return ans2-ans1