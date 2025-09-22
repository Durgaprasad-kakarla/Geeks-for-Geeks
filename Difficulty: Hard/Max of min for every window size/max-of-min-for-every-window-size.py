class Solution:
    def maxOfMins(self, arr):
       # code here
        def next_smaller(arr):
            n=len(arr)
            next=[n]*n
            stack=[]
            for i in range(n-1,-1,-1):
                while stack and arr[stack[-1]]>=arr[i]:
                    stack.pop()
                if stack:
                    next[i]=stack[-1]
                stack.append(i)
            return next
        def prev_smaller(arr):
            n=len(arr)
            prev=[-1]*n
            stack=[]
            for i in range(n):
                while stack and arr[stack[-1]]>=arr[i]:
                    stack.pop()
                if stack:
                    prev[i]=stack[-1]
                stack.append(i)
            return prev
        n=len(arr)
        next=next_smaller(arr)
        prev=prev_smaller(arr)
        res=[float('-inf') for  i in range(n)]
        for i in range(n):
            ind=next[i]-prev[i]-2
            res[ind]=max(res[ind],arr[i])
        stack=[]
        for i in range(n-1,-1,-1):
            while stack and res[stack[-1]]<res[i]:
                stack.pop()
            if stack:
                res[i]=max(res[i],res[stack[-1]])
            stack.append(i)
        return res