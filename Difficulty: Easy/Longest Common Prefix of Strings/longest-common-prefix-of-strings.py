#User function Template for python3
class TrieNode:
    def __init__(self):
        self.links=[None]*26
        self.cntEndsWith=0
        self.cntStartsWith=0
    def contains_key(self,ch):
        return self.links[ord(ch)-ord('a')] is not None
    def put(self,ch,node):
        self.links[ord(ch)-ord('a')]=node
    def get(self,ch):
        return self.links[ord(ch)-ord('a')]
    def increaseEnd(self):
        self.cntEndsWith+=1
    def increasePrefix(self):
        self.cntStartsWith+=1
    def decreaseEnd(self):
        self.cntEndsWith-=1
    def decreaseEnd(self):
        self.cntStartsWith-=1
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        node=self.root
        for ch in word:
            if not node.contains_key(ch):
                node.put(ch,TrieNode())
            node=node.get(ch)
            node.increasePrefix()
        node.increaseEnd()
class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        n=len(arr)
        mini=float('inf')
        for i in arr:
            if mini>len(i):
                mini=len(i)
                s=i
        st=""
        for i in range(mini):
            flag=0
            for j in range(n):
                if arr[j][i]!=s[i]:
                    flag=1
                    break
            if flag==0:
                st+=s[i]
            else:
                break
        return st if st!="" else -1
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        arr = [x for x in input().strip().split(" ")]

        ob = Solution()
        print(ob.longestCommonPrefix(arr))

# } Driver Code Ends