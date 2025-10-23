class Solution:
    def kClosest(self, points, k):
        # code here
        k_closest_lst=[]
        for i,j in points:
            k_closest_lst.append([i*i+j*j,i,j])
        k_closest_lst.sort()
        return [(i,j) for d,i,j in k_closest_lst[:k]]
        
        