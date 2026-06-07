from collections import deque
class Solution:
    def profession(self, level, pos):
        # code here
        def find_profession(pos,profession):
            while pos>1:
                if pos%2!=0:
                    profession=not profession
                pos//=2
            # print(pos,profession)
            if pos==0 and profession==0:
                return True
            if pos==1 and profession==1:
                return True
            return False
        if find_profession(pos-1,0):
            return "Engineer"
        return "Doctor"
        
'''
 1 2 3 1 3  2  1  2  3
0 1 3 6 7 10 12 13 15 18
2 4 5 8 9 11 14
 2 1 3 1 2 3
'''