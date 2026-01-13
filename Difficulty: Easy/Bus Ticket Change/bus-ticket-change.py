class Solution:
    def canServe(self, arr):
        # code here 
        n=len(arr)
        cnt_5,cnt_10=0,0
        for i in range(n):
            if arr[i]==5:
                cnt_5+=1
            elif arr[i]==10:
                if cnt_5>0:
                    cnt_5-=1
                    cnt_10+=1
                else:
                    return False
            else:
                if cnt_10>0 and cnt_5>0:
                    cnt_10-=1
                    cnt_5-=1
                elif cnt_5>2:
                    cnt_5-=3
                else:
                    return False
        return True
        