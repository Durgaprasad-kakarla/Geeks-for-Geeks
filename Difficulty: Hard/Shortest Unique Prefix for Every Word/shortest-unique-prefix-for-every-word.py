class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.count = 0


class Solution:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for ch in word:
            idx = ord(ch) - ord('a')

            if curr.child[idx] is None:
                curr.child[idx] = TrieNode()

            curr = curr.child[idx]
            curr.count += 1

    def getPrefix(self, word):
        curr = self.root
        prefix = []

        for ch in word:
            idx = ord(ch) - ord('a')
            curr = curr.child[idx]
            prefix.append(ch)

            if curr.count == 1:
                break

        return "".join(prefix)

    def findPrefixes(self, arr):
        for word in arr:
            self.insert(word)

        ans = []

        for word in arr:
            ans.append(self.getPrefix(word))

        return ans