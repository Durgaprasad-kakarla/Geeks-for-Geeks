#User function Template for python3
from collections import Counter
class Solution:
    def minIncrements(self, arr): 
        # Code here
        n = len(arr)
        arr.sort()
        lst = []
    
        # Collect ranges where numbers are missing
        for i in range(1, n):
            if arr[i] != arr[i - 1] and arr[i] != arr[i - 1] + 1:
                lst.append([arr[i - 1] + 1, arr[i] - 1])
    
        dic = Counter(arr)
        x = arr[-1] + 1
        tot = 0
        lst_index = 0
        for i in dic:
            if dic[i] > 1:
                cnt = dic[i] - 1
    
                while lst_index < len(lst) and lst[lst_index][0] < i:
                    lst_index += 1
    
                while lst_index < len(lst) and cnt > 0:
                    start, end = lst[lst_index]
                    length = end - start + 1
                    if length <= cnt:
                        tot += (start - i) * length + (length * (length - 1)) // 2
                        cnt -= length
                        lst_index += 1
                    else:
                        tot += (start - i) * cnt + (cnt * (cnt - 1)) // 2
                        lst[lst_index][0] += cnt  
                        cnt = 0
                if cnt > 0:
                    tot += (x - i) * cnt + (cnt * (cnt - 1)) // 2
                    x += cnt
    
        return tot
                    
                   
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    T = int(input())
    while T > 0:
        arr = [int(i) for i in input().split()]
        ob = Solution()
        print(ob.minIncrements(arr))

        T -= 1

# } Driver Code Ends