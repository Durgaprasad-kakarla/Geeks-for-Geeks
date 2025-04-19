#User function Template for python3
class TrieNode:
    def __init__(self):
        self.bits=[None]*2
    def contains_key(self,b):
        return self.bits[b] is not None
    def put_key(self,b,node):
        self.bits[b]=node
    def get_key(self,b):
        return self.bits[b]

class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,number):
        node=self.root
        for i in range(31,-1,-1):
            x=(number>>i)&1
            if not node.contains_key(x):
                node.put_key(x,TrieNode())
            node=node.get_key(x)
class Solution:
    def maxXor(self, arr):
        #code here
        t=Trie()
        tot=0
        for ele in arr:
            t.insert(ele)
        maxi=0
        for ele in arr:
            tot=0
            node=t.root
            for i in range(31,-1,-1):
                x=0 if (ele>>i)&1 else 1
                if node.contains_key(x):
                    tot+=(2**i)
                    node=node.get_key(x)
                else:
                    y=0 if x else 1
                    node=node.get_key(y)
            maxi=max(maxi,tot)
        return maxi


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        ob = Solution()
        print(ob.maxXor(arr))
        print("~")

# } Driver Code Ends