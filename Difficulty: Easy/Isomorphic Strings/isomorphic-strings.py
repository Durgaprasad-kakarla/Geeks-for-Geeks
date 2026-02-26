class Solution:
    def areIsomorphic(self, s1, s2):
        # code here 
        s1_dic,s2_dic={},{}
        n,m=len(s1),len(s2)
        for i in range(n):
            if s1[i] in s1_dic and s1_dic[s1[i]]!=s2[i]:
                return False
            if s2[i] in s2_dic and s2_dic[s2[i]]!=s1[i]:
                return False
            s1_dic[s1[i]]=s2[i]
            s2_dic[s2[i]]=s1[i]
        return True