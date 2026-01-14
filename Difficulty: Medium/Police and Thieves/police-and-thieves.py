from collections import deque
class Solution:
    def catchThieves(self, arr, k):
        #code here
        theif_queue,police_queue=deque(),deque()
        n=len(arr)
        cnt=0
        for i in range(n):
            # print('prev',police_queue,theif_queue)
            while theif_queue and theif_queue[0]<(i-k):
                theif_queue.popleft()
            while police_queue and police_queue[0]<(i-k):
                police_queue.popleft()
            # print(police_queue,theif_queue)
            if arr[i]=='P':
                if theif_queue:
                    theif_queue.popleft()
                    cnt+=1
                else:
                    police_queue.append(i)
            else:
                if police_queue:
                    police_queue.popleft()
                    cnt+=1
                else:
                    theif_queue.append(i)
            
        return cnt
