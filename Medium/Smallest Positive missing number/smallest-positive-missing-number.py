#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,nums,n):
        #Your code here
        nums=list(set(nums))
        nums.sort()
        res=1
        for i in range(len(nums)):
            if nums[i]>0:
                if nums[i]!=res:
                    return res
                else:
                    res+=1
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3


import math


def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            print(ob.missingNumber(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends