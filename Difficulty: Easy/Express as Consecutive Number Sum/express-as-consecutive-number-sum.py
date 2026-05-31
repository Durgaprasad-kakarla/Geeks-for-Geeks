class Solution:
    def isSumOfConsecutive(self, n: int) -> bool:
        # code here
        if n&1:
            if n<2:
                return False
            return True
        else:
            while n>1 and n%2==0:
                n=n//2
            if n>1:
                return True
            return False