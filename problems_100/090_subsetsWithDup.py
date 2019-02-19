'''
给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。

说明：解集不能包含重复的子集。

示例:

输入: [1,2,2]
输出:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
'''


'''
68 ms, 6.7 MB
'''
from collections import defaultdict
class Solution:
    def helper(self, d):
        if not d: return [[]]
        result = []
        for k in d:
            k, v = k, d[k]
            break
        del d[k]
        temp = self.helper(d)
        for i in range(v + 1):
            for t in temp:
                result.append([k] * i + t)
        return result

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        count = defaultdict(int)
        for i in nums:
            count[i] += 1
        return self.helper(count)


'''
52 ms, 6.6 MB
'''
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        index = 0
        path = []
        res = []
        self.helper(index, nums, path, res)
        return res

    def helper(self, index, nums, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]: continue
            self.helper(i+1, nums, path + [nums[i]], res)
