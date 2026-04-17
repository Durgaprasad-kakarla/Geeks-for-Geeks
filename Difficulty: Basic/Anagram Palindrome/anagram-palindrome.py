class Solution:
    def canFormPalindrome(n,s)->bool:
        # code here
        # print(s)
        n=len(s)
        dic={}
        for i in range(n):
            if s[i] in dic:
                dic[s[i]]+=1
            else:
                dic[s[i]]=1
        cnt=0
        # print(dic)
        for i in dic:
            if dic[i]%2!=0:
                cnt+=1
        return cnt<2
            