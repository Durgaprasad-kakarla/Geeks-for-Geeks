class Solution:
    def subarrayRanges(self, arr):
        # Code here
        n=len(arr)
        def minimum_sum(arr):
            stack=[(-float('inf'),0)]
            tot=0
            for i in range(n):
                while stack and stack[-1][0]>=arr[i]:
                    ele,ind=stack.pop()
                    tot+=(i-ind+1)*ele*(ind-stack[-1][1])
                stack.append((arr[i],i+1))
            while len(stack)>1:
                ele,ind=stack.pop()
                tot+=(n-ind+1)*ele*(ind-stack[-1][1])
            return tot
        def maximum_sum(arr):
            stack=[(float('inf'),0)]
            tot=0
            for i in range(n):
                while stack and stack[-1][0]<=arr[i]:
                    ele,ind=stack.pop()
                    tot+=(i-ind+1)*ele*(ind-stack[-1][1])
                stack.append((arr[i],i+1))
            while len(stack)>1:
                ele,ind=stack.pop()
                tot+=(n-ind+1)*ele*(ind-stack[-1][1])
            return tot
        return (maximum_sum(arr)-minimum_sum(arr))