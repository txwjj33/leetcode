'''
题目：合并区间
描述：
给出一个区间的集合，请合并所有重叠的区间。

示例 1:

输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2:

输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
'''

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e


'''
关键是先把keys排序，72 ms
'''
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0: return []
        dic = {}
        for v in intervals:
            if v.start not in dic:
                dic[v.start] = v.end
            else:
                dic[v.start] = max(dic[v.start], v.end)
        keys = list(dic.keys())
        keys.sort()

        result = []
        for k in keys:
            if len(result) > 0 and k <= result[-1][1]:
                if dic[k] > result[-1][1]:
                    result[-1][1] = dic[k]
            else:
                result.append([k, dic[k]])

        return result


'''
这跟上一个算法差不多，写法简化了不少，68 ms
'''
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key = lambda v: v.start)
        # intervals[:1]这种写法对于len(intervals) == 0也不会出问题
        result = intervals[:1]
        for v in intervals:
            if v.start <= result[-1].end:
                if v.end > result[-1].end:
                    result[-1].end = v.end
            else:
                result.append(v)

        return result
