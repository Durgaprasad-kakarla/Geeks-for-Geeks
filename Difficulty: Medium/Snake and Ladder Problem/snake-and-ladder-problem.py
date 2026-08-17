from queue import deque
class Solution:
    def minThrows(self, n, lad, sn):
        # code here
        sn_dic,lad_dic={},{}
        for i in range(0,len(sn),2):
            sn_dic[sn[i]]=sn[i+1]
        for i in range(0,len(lad),2):
            lad_dic[lad[i]]=lad[i+1]
            
        queue=deque([(1,0)])
        vis=set()
        vis.add(1)
        while queue:
            node,d=queue.popleft()
            if node>n*n:
                continue    
            if node==n*n:
                return d
            for i in range(1,7):
                nxt=node+i
                if nxt in sn_dic:
                    nxt=sn_dic[nxt]
                elif nxt in lad_dic:
                    nxt=lad_dic[nxt]
                if nxt not in vis:
                    vis.add(nxt)
                    queue.append((nxt,d+1))
        return -1
        #     for i in range(1,7):
        #         if ind+i in sn_dic and sn_dic[ind+i] not in vis:
        #             mini=min(mini,1+min_throws(sn_dic[ind+i]))
        #         elif ind+i in lad_dic and lad_dic[ind+i] not in vis:
        #             mini=min(mini,1+min_throws(lad_dic[ind+i]))
        #         elif ind+i not in vis:
        #             mini=min(mini,1+min_throws(ind+i))
        #     # dp[ind]=mini
        #     return mini
        # dp=[-1 for _ in range(n*n+1)]
        # vis=set()
        # return min_throws(1)