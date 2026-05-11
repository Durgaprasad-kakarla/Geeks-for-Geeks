class Solution:
    def palindromePair(self, arr):
        # Code here
        def check_palindrome(s):
            return s==s[::-1]
        def check_match(s1,s2):
            return s1==s2
        n=len(arr)
        words_lst={arr[i]:i for i in range(n)}
        for i in range(n):
            word=arr[i]
            k=len(word)
            for j in range(k):
                curr=word[:j+1][::-1]
                if curr in words_lst and words_lst[curr]!=i:
                    if check_palindrome(word[j+1:]):
                        return True
            for j in range(k):
                curr=word[j:][::-1]
                # print(curr)
                if curr in words_lst and words_lst[curr]!=i:
                    if check_palindrome(word[:j]):
                        return True
        return False