class Solution:
    def assignHole(self, mices, holes):
        # code here
        mices.sort()
        holes.sort()
        maxi=-float('inf')
        n=len(mices)
        for i in range(n):
            maxi=max(maxi,abs(mices[i]-holes[i]))
        return maxi
        