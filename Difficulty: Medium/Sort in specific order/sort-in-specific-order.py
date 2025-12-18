class Solution:
    def sortIt(self, arr):
        # code here
        n=len(arr)
        odd,even=[],[]
        for i in range(n):
            if arr[i]&1:
                odd.append(arr[i])
            else:
                even.append(arr[i])
        lst=sorted(odd,reverse=True)+sorted(even)
        for i in range(n):
            arr[i]=lst[i]
        return arr
    
