#{ 
 # Driver Code Starts
#Initial Template for Python 3
import sys


# } Driver Code Ends

#User function Template for python3
from collections import deque
class Solution:
    def findOrder(words):
        # code here
        n=len(words)
        st=set()
        for i in range(n):
            for j in range(len(words[i])):
                st.add(ord(words[i][j])-97)
        adj=[[] for i in range(26)]
        indegree=[0]*26
        for i in range(1,n):
            word1,word2=words[i-1],words[i]
            len1,len2=len(word1),len(word2)
            flag=0
            for j in range(min(len1,len2)):
                if word1[j]!=word2[j]:
                    adj[ord(word1[j])-97].append(ord(word2[j])-97)
                    indegree[ord(word2[j])-97]+=1
                    flag=1
                    break
            if flag==0:
                if len1>len2:
                    return ""
        # print(st)
        topo=[]
        queue=deque()
        for i in range(26):
            # print(indegree[i],i in st)
            if indegree[i]==0 and i in st:
                queue.append(i)
        # print(queue)
        while queue:
            node=queue.popleft()
            topo.append(chr(97+node))
            for i in adj[node]:
                indegree[i]-=1
                if indegree[i]==0:
                    queue.append(i)
        return "".join(topo) if len(topo)==len(st) else ""

#{ 
 # Driver Code Starts.

def validate(original, order):
    char_map = {}
    for word in original:
        for ch in word:
            char_map[ch] = 1

    for ch in order:
        if ch not in char_map:
            return False
        del char_map[ch]

    if char_map:
        return False

    char_index = {ch: i for i, ch in enumerate(order)}

    for i in range(len(original) - 1):
        a, b = original[i], original[i + 1]
        k, n, m = 0, len(a), len(b)
        while k < n and k < m and a[k] == b[k]:
            k += 1
        if k < n and k < m and char_index[a[k]] > char_index[b[k]]:
            return False
        if k != n and k == m:
            return False

    return True

if __name__ == "__main__":
    input_data = sys.stdin.read().strip().split("\n")
    index = 0
    t = int(input_data[index])
    index += 1
    while t > 0:
        words = input_data[index].split()
        index += 1
        original = words[:]

        order = Solution.findOrder(words)

        if order == "":
            print("\"\"")
        else:
            print("true" if validate(original, order) else "false")
        print("~")
        t -= 1

# } Driver Code Ends