from collections import Counter
class Solution:
    def duplicates(self, arr, n): 
    	# code here
    	dic=Counter(arr)
    	lst=[]
    	for i in dic:
    	    if dic[i]>1:
    	        lst.append(i)
    	if not lst:
    	    return [-1]
    	return sorted(lst)


#{ 
 # Driver Code Starts
if(__name__=='__main__'):
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        res = Solution().duplicates(arr, n)
        for i in res:
            print(i,end=" ")
        print()



# } Driver Code Ends