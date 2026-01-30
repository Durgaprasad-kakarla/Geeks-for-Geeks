class Solution:
    def rearrangeQueue(self, queue):
        ans=[0]*len(queue)
        i=0
        while i<len(ans):
            node=queue.popleft()
            ans[i]=node
            i+=2
        i=1
        while i<len(ans):
            node=queue.popleft()
            ans[i]=node
            i+=2
        for i in range(len(ans)):
            queue.append(ans[i])
        return queue
            
        
'''
[1,2,3,4,5,6]

[1,4,2,5,3,6]   

[1,]


[1,6,2,5,3,4]

'''