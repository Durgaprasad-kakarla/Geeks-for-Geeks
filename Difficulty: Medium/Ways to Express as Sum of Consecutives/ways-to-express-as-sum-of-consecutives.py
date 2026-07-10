class Solution:
    def getCount(self, n):
        # code here 
        div = 2
        sub = 1
        c = 0
        while n > sub:
            if (n - sub) % div == 0:
                c += 1
            sub += div
            div += 1
        return c