from collections import deque
class Solution:
    def findOrder(self, words):
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