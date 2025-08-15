class Solution:
    def insertInterval(self, intervals, newInterval):
        # Code here
        intervals.append(newInterval)
        intervals.sort()
        ans,n=[],len(intervals)
        start,end=intervals[0]
        for i in range(1,n):
            s,e=intervals[i]
            if end>=s:
                end=max(end,e)
            else:
                ans.append([start,end])
                start,end=intervals[i]
        ans.append([start,end])
        return ans