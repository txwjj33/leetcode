'''
题目：插入区间
描述：
给出一个无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

示例 1:

输入: intervals = [[1,3],[6,9]], newInterval = [2,5]
输出: [[1,5],[6,9]]
示例 2:

输入: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出: [[1,2],[3,10],[12,16]]
解释: 这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


'''
二分查找插入以后，使用56题类似的算法，64 ms
'''
class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        # 二分查找第一个不小于newInterval.start的数
        left, right = 0, len(intervals)
        while left < right:
            mid = left + (right - left) // 2
            if intervals[mid].start < newInterval.start:
                left = mid + 1
            else:
                right = mid

        intervals.insert(left, newInterval)
        startIndex = max(left, 1)
        result = intervals[:startIndex]
        for i in range(startIndex, len(intervals)):
            v = intervals[i]
            if v.start <= result[-1].end:
                if v.end > result[-1].end:
                    result[-1].end = v.end
            else:
                if i > left:
                    # 后面的区间不会有重叠，直接加到result
                    result.extend(intervals[i:])
                else:
                    result.append(v)

        return result
