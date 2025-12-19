class Solution:
    def findMoves(self, chairs, passengers):
        # code here
        chairs.sort()
        passengers.sort()
        n=len(chairs)
        tot=0
        for i in range(n):
            tot+=abs(passengers[i]-chairs[i])
        return tot
