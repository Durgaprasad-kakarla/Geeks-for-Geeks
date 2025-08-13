class Solution:
    def minSoldiers(self, arr, k):
        # code here
        n=len(arr)
        if n%2==0:
            soldiers=n//2
        else:
            soldiers=n//2+1
        cnt,lst=0,[]
        for i in range(n):
            if arr[i]%k==0:
                cnt+=1
            else:
                lst.append(k-(arr[i]%k))
        if cnt>=soldiers:
            return 0
        mini_soldiers=0
        lst.sort()
        i=0
        while cnt<soldiers:
            mini_soldiers+=lst[i]
            cnt+=1
            i+=1
        return mini_soldiers
            