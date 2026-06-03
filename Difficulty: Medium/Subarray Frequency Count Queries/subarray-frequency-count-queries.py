import bisect
from collections import defaultdict
class Solution:
    def freqInRange(self, arr, queries):
        # code here
        index = defaultdict(list)
        for pos, num in enumerate(arr):
            index[num].append(pos)
        
        # Prepare result array
        result = [0] * len(queries)
        
        # Process queries in value groups
        query_groups = defaultdict(list)
        for i, (l, r, val) in enumerate(queries):
            query_groups[val].append((l, r, i))
        
        # Process each value group
        for val in query_groups:
            if val not in index:
                continue  # Value never appears in array
            
            positions = index[val]
            len_pos = len(positions)
            
            # Optimize for common cases
            if len_pos < 100:  # For small counts, use linear scan
                for l, r, i in query_groups[val]:
                    count = 0
                    for pos in positions:
                        if l <= pos <= r:
                            count += 1
                    result[i] = count
            else:  # For large counts, use binary search
                for l, r, i in query_groups[val]:
                    left = bisect.bisect_left(positions, l)
                    right = bisect.bisect_right(positions, r)
                    result[i] = right - left
        
        return result