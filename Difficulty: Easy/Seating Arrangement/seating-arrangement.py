class Solution:
    def canSeatAllPeople(self, k, seats):
        # code here
        n=len(seats)
        for i in range(1,n):
            if seats[i-1]==1 and seats[i]==1:
                return False
        cnt=k
        for i in range(0,n,2):
            if seats[i]==1:
                continue
            else:
                if (i>0 and seats[i-1]==1) or (i<n-1 and seats[i+1]==1):
                    continue
                cnt-=1
        if cnt<=0:
            return True
        cnt=k
        for i in range(1,n,2):
            if seats[i]==1:
                continue
            else:
                if (i>0 and seats[i-1]==1) or (i<n-1 and seats[i+1]==1):
                    continue
                cnt-=1
        if cnt<=0:
            return True
        return False