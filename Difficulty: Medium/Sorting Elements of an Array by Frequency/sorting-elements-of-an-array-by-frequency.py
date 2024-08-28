#User function Template for python3
from collections import Counter
class Solution:
   
    #Function to sort the array according to frequency of elements.
    def sortByFreq(self,arr):
        #code here
        dic=Counter(arr)
        # print(arr)
        new_dic={}
        for i,d in dic.items():
            if d in new_dic:
                new_dic[d].append(i)
            else:
                new_dic[d]=[i]
        final=[]
        for i in sorted(new_dic,reverse=True):
            for j in sorted(new_dic[i]):
                final+=[j]*i 
        return final
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for tt in range(t):

        arr = list(map(int, input().strip().split()))
        l = Solution().sortByFreq(arr)
        print(*l)

# } Driver Code Ends