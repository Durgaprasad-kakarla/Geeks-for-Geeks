class Solution:
    def asciirange(self, s):
        # code here
        n=len(s)
        chars_first_last=[[-1,-1] for i in range(26)]
        pref=[0]*(n+1)
        for i in range(n):
            if chars_first_last[ord(s[i])-97][0]==-1:
                chars_first_last[ord(s[i])-97][0]=i
            else:
                chars_first_last[ord(s[i])-97][1]=i
            pref[i+1]+=pref[i]+ord(s[i])
        # print(pref,chars_first_last)
        ans=[]
        for i in range(26):
            first,last=chars_first_last[i][0],chars_first_last[i][1]
            if first!=-1 and last!=-1 and pref[last]>pref[first+1]:
                ans.append(pref[last]-pref[first+1])
        return ans