#User function Template for python3


class Solution:

    def anagrams(self, arr):
        n=len(arr)
        for i in range(n):
            s="".join(sorted(arr[i]))
            arr[i]=[s,i,arr[i]]
        arr.sort()
        final=[]
        curr=[arr[0][2]]
        for i in range(1,n):
            if arr[i][0]==arr[i-1][0]:
                curr.append(arr[i][2])
            else:
                final.append(curr)
                curr=[arr[i][2]]
        final.append(curr)
        return final



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
    t = int(input())
    for tcs in range(t):
        words = input().split()

        ob = Solution()
        ans = ob.anagrams(words)

        for grp in sorted(ans):
            for word in grp:
                print(word, end=' ')
            print()

        print("~")

# } Driver Code Ends