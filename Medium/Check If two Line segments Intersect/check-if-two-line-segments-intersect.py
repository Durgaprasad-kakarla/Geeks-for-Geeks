#User function Template for python3
class Solution:
    def doIntersect(self, p1, q1, p2, q2):
        #code here
        def onSegment(p, q, r): 
            if ( (q[0] <= max(p[0], r[0])) and (q[0] >= min(p[0], r[0])) and 
                   (q[1] <= max(p[1], r[1])) and (q[1] >= min(p[1], r[1]))): 
                return True
            return False
          
        def orientation(p, q, r): 
              
            val = (float(q[1] - p[1]) * (r[0] - q[0])) - (float(q[0] - p[0]) * (r[1] - q[1])) 
            if (val > 0): 
                return 1
            elif (val < 0):
                return 2
            else:
                return 0
        o1 = orientation(p1, q1, p2) 
        o2 = orientation(p1, q1, q2) 
        o3 = orientation(p2, q2, p1) 
        o4 = orientation(p2, q2, q1) 
      
        # General case 
        if ((o1 != o2) and (o3 != o4)): 
            return "true"
      
        # Special Cases 
      
        # p1 , q1 and p2 are collinear and p2 lies on segment p1q1 
        if ((o1 == 0) and onSegment(p1, p2, q1)): 
            return "true"
      
        # p1 , q1 and q2 are collinear and q2 lies on segment p1q1 
        if ((o2 == 0) and onSegment(p1, q2, q1)): 
            return "true"
      
        # p2 , q2 and p1 are collinear and p1 lies on segment p2q2 
        if ((o3 == 0) and onSegment(p2, p1, q2)): 
            return "true"
      
        # p2 , q2 and q1 are collinear and q1 lies on segment p2q2 
        if ((o4 == 0) and onSegment(p2, q1, q2)): 
            return "true"
      
        # If none of the cases 
        return "false"


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1 = list(map(int, input().strip().split(" ")))
        S2 = list(map(int, input().strip().split(" ")))
        p1 = []
        q1 = []
        p2 = []
        q2 = []
        p1.append(S1[0])
        p1.append(S1[1])
        q1.append(S1[2])
        q1.append(S1[3])
        p2.append(S2[0])
        p2.append(S2[1])
        q2.append(S2[2])
        q2.append(S2[3])
        ob = Solution()
        ans = ob.doIntersect(p1, q1, p2, q2)
        print(ans)

# } Driver Code Ends