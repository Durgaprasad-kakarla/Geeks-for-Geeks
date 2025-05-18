# function should return parent of x
def find(par, x):
    # Code here
    if par[x-1]==x:
        return x
    par[x-1]=find(par,par[x-1])
    return par[x-1]

# function shouldn't return or print anything
def unionSet(par, x, z):
    # Code here
    ulp_u=find(par,x)
    ulp_v=find(par,z)
    par[ulp_u-1]=ulp_v
    return 
    



#{ 
 # Driver Code Starts
if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n, k = list(map(int, input().strip().split()))
        arr = [x for x in range(1, n + 1)]
        s = input().strip().split()
        i = 0
        while i < len(s):
            if s[i] == 'FIND':
                print(find(arr, int(s[i + 1])), end=" ")
                i += 2
            elif s[i] == 'UNION':
                unionSet(arr, int(s[i + 1]), int(s[i + 2]))
                i += 3
        print()
        print("~")

# } Driver Code Ends