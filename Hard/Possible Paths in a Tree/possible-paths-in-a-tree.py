#User function Template for python3

class Solution:
    def maximumWeight(self, n, edges, q, queries):
        # code here
        unionfind=list(range(n))
        size=[1]*n
        def util(x):
            if unionfind[x]!=x:
                unionfind[x]=util(unionfind[x])
            return unionfind[x]
        edges.sort(key=lambda x:x[2],reverse=True)
        queries=sorted(enumerate(queries),key=lambda x:x[1])
        res=[0]*q
        curr=0
        for index,i in queries:
            while edges and edges[-1][2]<=i:
                x,y,_=edges.pop()
                x,y=util(x-1),util(y-1)
                if x!=y:
                    unionfind[x]=y
                    curr+=size[x]*size[y]
                    size[y]+=size[x]
            res[index]=curr
        return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())

        edges = [[0 for j in range(3)] for i in range(n-1)]
        for i in range(n-1):
            input_line = [int(x) for x in input().strip().split()]       
            for j in range (3):
                edges[i][j]=input_line[j]

        q = int(input())
        queries = list(map(int, input().strip().split()))

        ob = Solution()
        ans = ob.maximumWeight(n, edges, q, queries)
        for i in ans:
            print(i,end=" ")
        print()


# } Driver Code Ends