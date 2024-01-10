#User function Template for python3
class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, k) : 
		#Complete the function
        pref=0
        dic={}
        maxi=0
        for i in range(n):
            pref+=arr[i]
            mod = ((pref % k) + k) % k
            if mod == 0:
                maxi = i + 1
            elif mod in dic:
                if maxi < (i - dic[mod]):
                    maxi = i - dic[mod]
            else:
                dic[mod] = i
        return maxi



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends