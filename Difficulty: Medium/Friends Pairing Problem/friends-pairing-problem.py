class Solution:
    def countFriendsPairings(self, n: int) -> int:
        # code here 
        if n<=2:
            return n
        return self.countFriendsPairings(n-1)+(n-1)*self.countFriendsPairings(n-2)