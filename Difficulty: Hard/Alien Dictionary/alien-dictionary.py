#User function Template for python3

class Solution:
    def findOrder(self,dic, n, k):
        # code here
        adj=[[] for i in range(k)]
        for ind in range(1,n):
            prev=dic[ind-1]
            curr=dic[ind]
            for i in range(min(len(prev),len(curr))):
                if prev[i]!=curr[i]:
                    adj[ord(prev[i])-97].append(ord(curr[i])-97)
                    break
        # print(adj)
        def dfs(node,vis,stack,adj):
            vis[node]=1
            for i in adj[node]:
                if not vis[i]:
                    dfs(i,vis,stack,adj)
            stack.append(node)
        def topological_sort(adj):
            n=len(adj)
            vis=[0 for i in range(n)]
            stack=[]
            for i in range(n):
                if not vis[i]:
                    dfs(i,vis,stack,adj)
            return stack[::-1]
        topo=(topological_sort(adj))
        alien_order=[]
        for i in topo:
            alien_order.append(chr(97+i))
        return alien_order


#{ 
 # Driver Code Starts
#Initial Template for Python 3

class sort_by_order:
    def __init__(self,s):
        self.priority = {}
        for i in range(len(s)):
            self.priority[s[i]] = i
    
    def transform(self,word):
        new_word = ''
        for c in word:
            new_word += chr( ord('a') + self.priority[c] )
        return new_word
    
    def sort_this_list(self,lst):
        lst.sort(key = self.transform)

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        line=input().strip().split()
        n=int(line[0])
        k=int(line[1])
        
        alien_dict = [x for x in input().strip().split()]
        duplicate_dict = alien_dict.copy()
        ob=Solution()
        order = ob.findOrder(alien_dict,n,k)
        s = ""
        for i in range(k):
            s += chr(97+i)
        l = list(order)
        l.sort()
        l = "".join(l)
        if s != l:
            print(0)
        else:
            x = sort_by_order(order)
            x.sort_this_list(duplicate_dict)
            
            if duplicate_dict == alien_dict:
                print(1)
            else:
                print(0)


# } Driver Code Ends