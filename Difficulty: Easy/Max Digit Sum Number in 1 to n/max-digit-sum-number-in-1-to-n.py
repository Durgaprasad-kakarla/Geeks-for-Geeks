class Solution:
    def findMax(self, n):
        # code here
        s=(str(n))
        k=len(s)
        pref=[0]*(k+1)
        for i in range(1,k+1):
            pref[i]+=(pref[i-1]+int(s[i-1]))
        def get_max_digit_sm(ind):
            curr_lst=lst.copy()
            for i in range(ind+1,len(curr_lst)):
                curr_lst[i]='9'
            if ind<k-1:
                for i in range(ind,-1,-1):
                    if lst[ind]!='0':
                        curr_lst[ind]=str(int(lst[i])-1)
                        break
            tot=0
            for i in range(len(curr_lst)):
                tot+=int(curr_lst[i])
            return curr_lst,tot
        maxi=-float('inf')
        ele=n
        lst=list(s)
        for i in range(k-1,-1,-1):
            curr_lst,k=get_max_digit_sm(i)
            # print(curr_lst,k)
            if maxi<k:
                maxi=k
                ele=int("".join(curr_lst))
        return ele
        