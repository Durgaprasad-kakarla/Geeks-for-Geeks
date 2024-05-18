#User function Template for python3

#Function to push an element in queue by using 2 stacks.
def Push(x,stack1,stack2):
    stack1.append(x)

#Function to pop an element from queue by using 2 stacks.
def Pop(stack1,stack2):
    if stack2:
        return stack2.pop()
    else:
        while stack1:
            stack2.append(stack1.pop())
        if stack2:
            return stack2.pop()
        return -1
    #code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        qry=int(input())
        qtyp_qry=list(map(int, input().strip().split()))
        
        i=0
        stack1=[]
        stack2=[]
        while i <len(qtyp_qry):
            #print(i)
            if qtyp_qry[i]==1:
                Push(qtyp_qry[i+1],stack1,stack2)
                #print(i)
                i+=2
            else:
                print(Pop(stack1,stack2),end=' ')
                i+=1
                
        print()
# } Driver Code Ends