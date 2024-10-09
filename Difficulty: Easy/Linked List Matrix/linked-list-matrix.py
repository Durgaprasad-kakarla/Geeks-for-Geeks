#User function Template for python3

'''

class Node():
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down=None

'''

class Solution:
    def constructLinkedMatrix(self, mat):
        #your code goes here
        head=Node(mat[0][0])
        n,m=len(mat),len(mat[0])
        new_mat=[[None for i in range(m)] for j in range(n)]
        new_mat[0][0]=head
        for i in range(n):
            for j in range(m):
                new_node=new_mat[i][j]
                if j+1<m:
                    if new_mat[i][j+1] is None:
                        right_node=Node(mat[i][j+1])
                        new_node.right=right_node
                        new_mat[i][j+1]=right_node
                    else:
                        new_node.right=new_mat[i][j+1]
                if i+1<n:
                    if new_mat[i+1][j] is None:
                        down_node=Node(mat[i+1][j])
                        new_node.down=down_node
                        new_mat[i+1][j]=down_node
                    else:
                        new_node.down=new_mat[i+1][j]
        return head

#{ 
 # Driver Code Starts
class Node():

    def __init__(self, x):
        self.data = x
        self.right = None
        self.down = None


def display(head):
    Dp = head
    while Dp:
        Rp = Dp
        while Rp:
            print(Rp.data, end=" ")
            if Rp.right:
                print(Rp.right.data, end=" ")
            else:
                print("null", end=" ")
            if Rp.down:
                print(Rp.down.data, end=" ")
            else:
                print("null", end=" ")
            Rp = Rp.right
        Dp = Dp.down


if __name__ == "__main__":
    for _ in range(int(input())):
        # First row input
        a = list(map(int, input().strip().split()))
        n = len(a)

        # Input the matrix
        mat = [a]
        for i in range(1, n):
            row = list(map(int, input().strip().split()))
            mat.append(row)

        # Create a Solution object and construct the linked matrix
        obj = Solution()
        head = obj.constructLinkedMatrix(mat)
        if head is None:
            print(-1)
            continue
        display(head)
        print()

# } Driver Code Ends