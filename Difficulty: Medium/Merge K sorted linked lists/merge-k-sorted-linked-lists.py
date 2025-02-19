#User function Template for python3
'''
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None
'''
import heapq
class Solution:
    def mergeKLists(self, lists):
        # code here
        # return head of merged list
        heap=[]
        for head in lists:
            temp=head
            while temp:
                heapq.heappush(heap,temp.data)
                temp=temp.next
        if not heap:
            return None
        head=Node(heapq.heappop(heap))
        temp=head
        while heap:
            temp.next=Node(heapq.heappop(heap))
            temp=temp.next
        return head

#{ 
 # Driver Code Starts
import heapq


class Node:

    def __init__(self, x):
        self.data = x
        self.next = None

    # To compare nodes in the heap
    def __lt__(self, other):
        return self.data < other.data


def printList(node):
    while node:
        print(node.data, end=" ")
        node = node.next
    print()


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lists = []
        for _ in range(n):
            values = list(map(int, input().split()))
            head = None
            temp = None
            for value in values:
                newNode = Node(value)
                if head is None:
                    head = newNode
                    temp = head
                else:
                    temp.next = newNode
                    temp = temp.next
            lists.append(head)

        sol = Solution()
        head = sol.mergeKLists(lists)
        printList(head)
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends