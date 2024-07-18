#User function Template for python3
class Solution: 
    # Function to find the maximum length of alternating subsequence
    def alternatingMaxLength(self, arr):
       #code here
        prev_symbol,prev_element,tot,n='',arr[0],1,len(arr)
        for i in range(1,n):
            if prev_element<arr[i]:
                if prev_symbol!='<':
                    tot+=1
                    prev_symbol='<'
                    prev_element=arr[i]
                else:
                    prev_element=max(prev_element,arr[i])
            elif prev_element>arr[i]:
                if prev_symbol!='>':
                    tot+=1
                    prev_symbol='>'
                    prev_element=arr[i]
                else:
                    prev_element=min(prev_element,arr[i])
            else:
                continue
        return tot


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    tc = int(data[0])
    for i in range(1, tc + 1):
        s = data[i].strip().split()
        nums = list(map(int, s))
        obj = Solution()
        ans = obj.alternatingMaxLength(nums)
        print(ans)

# } Driver Code Ends