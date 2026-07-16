class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        
        intervals.sort()
        ans = [intervals[0]]

        for i in range(1, len(intervals)):
            last = ans[-1]
            if intervals[i][0]<=last[1]:
                last[1]= max(last[1], intervals[i][1])
            else:
                ans. append(intervals[i])

        return ans