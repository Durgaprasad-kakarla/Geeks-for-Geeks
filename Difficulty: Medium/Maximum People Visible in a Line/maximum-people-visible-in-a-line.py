class Solution:
    def maxPeople(self, arr):
        # code here
        n=len(arr)
        def next_large(arr):
            stack=[]
            next_larger=[-1]*n
            for i in range(n-1,-1,-1):
                while stack and stack[-1][0]<arr[i]:
                    stack.pop()
                if stack:
                    next_larger[i]=stack[-1][1]
                else:
                    next_larger[i]=n
                stack.append([arr[i],i])
            return next_larger
        def prev_large(arr):
            stack=[]
            prev_larger=[-1]*n
            for i in range(n):
                while stack and stack[-1][0]<arr[i]:
                    stack.pop()
                if stack:
                    prev_larger[i]=stack[-1][1]
                else:
                    prev_larger[i]=-1
                stack.append([arr[i],i])
            return prev_larger
        # print(next_large(arr))
        # print(prev_large(arr))
        maxi=0
        next_larger,prev_larger=next_large(arr),prev_large(arr)
        for i in range(n):
            maxi=max(maxi,next_larger[i]-prev_larger[i]-1)
        return maxi