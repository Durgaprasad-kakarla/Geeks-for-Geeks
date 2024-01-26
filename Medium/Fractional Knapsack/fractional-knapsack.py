#User function Template for python3

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        dic={}
        for i in range(n):
            ratio=(arr[i].value/arr[i].weight)
            if ratio in dic:
                dic[ratio]=[arr[i].value+dic[ratio][0],arr[i].weight+dic[ratio][1]]
            else:
                dic[ratio]=[arr[i].value,arr[i].weight]
        lst=sorted(dic,reverse=True)
        n=len(lst)
        i=0
        tot=0
        while W>0 and i<n:
            val,wt=dic[lst[i]]
            if wt<=W:
                tot+=val
                W-=wt
            else:
                tot+=(val*(W/wt))
                break
            i+=1
        return tot
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,W = map(int,input().strip().split())
        info = list(map(int,input().strip().split()))
        arr = [Item(0,0) for i in range(n)]
        for i in range(n):
            arr[i].value = info[2*i]
            arr[i].weight = info[2*i+1]
            
        ob=Solution()
        print("%.6f" %ob.fractionalknapsack(W,arr,n))

# } Driver Code Ends